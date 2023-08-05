# -*- coding: utf-8 -*-

import typing as T
import enum
import dataclasses
from datetime import datetime

from light_emoji import common as emojis
from boto_session_manager import BotoSesManager

from ..tagging import to_tag_list
from ..helper import vprint
from ..waiter import Waiter

from .human_task_ui import (
    get_task_template_arn,
)


# --- Data Model
@dataclasses.dataclass
class HumanLoopConfig:
    work_team_arn: T.Optional[str] = dataclasses.field(default=None)
    human_task_ui_arn: T.Optional[str] = dataclasses.field(default=None)
    task_title: T.Optional[str] = dataclasses.field(default=None)
    task_description: T.Optional[str] = dataclasses.field(default=None)
    task_count: T.Optional[int] = dataclasses.field(default=None)
    task_availability_lifetime_in_seconds: T.Optional[int] = dataclasses.field(
        default=None
    )
    task_time_limit_in_seconds: T.Optional[int] = dataclasses.field(default=None)

    @property
    def human_task_ui_name(self) -> str:
        return self.task_title


@dataclasses.dataclass
class OutputConfig:
    s3_output_path: T.Optional[str] = dataclasses.field(default=None)
    kms_key_id: T.Optional[str] = dataclasses.field(default=None)


class FlowDefinitionStatusEnum(str, enum.Enum):
    Initializing = "Initializing"
    Active = "Active"
    Failed = "Failed"
    Deleting = "Deleting"


@dataclasses.dataclass
class FlowDefinition:
    arn: T.Optional[str] = dataclasses.field(default=None)
    name: T.Optional[str] = dataclasses.field(default=None)
    status: T.Optional[str] = dataclasses.field(default=None)
    creation_time: T.Optional[datetime] = dataclasses.field(default=None)
    role_arn: T.Optional[str] = dataclasses.field(default=None)
    human_loop_config: T.Optional[HumanLoopConfig] = dataclasses.field(default=None)
    output_config: T.Optional[OutputConfig] = dataclasses.field(default=None)

    @classmethod
    def from_describe_flow_definition_response(cls, response: dict) -> "FlowDefinition":
        return cls(
            arn=response["FlowDefinitionArn"],
            name=response["FlowDefinitionName"],
            status=response["FlowDefinitionStatus"],
            role_arn=response["RoleArn"],
            creation_time=response["CreationTime"],
            human_loop_config=HumanLoopConfig(
                work_team_arn=response["HumanLoopConfig"]["WorkteamArn"],
                human_task_ui_arn=response["HumanLoopConfig"]["HumanTaskUiArn"],
                task_title=response["HumanLoopConfig"]["TaskTitle"],
                task_description=response["HumanLoopConfig"]["TaskDescription"],
                task_count=response["HumanLoopConfig"]["TaskCount"],
                task_availability_lifetime_in_seconds=response["HumanLoopConfig"].get(
                    "TaskAvailabilityLifetimeInSeconds"
                ),
                task_time_limit_in_seconds=response["HumanLoopConfig"].get(
                    "TaskTimeLimitInSeconds"
                ),
            ),
            output_config=OutputConfig(
                s3_output_path=response["OutputConfig"]["S3OutputPath"],
                kms_key_id=response["OutputConfig"].get("KmsKeyId"),
            ),
        )


# --- Low level API
def get_flow_definition_arn(
    aws_account_id: str,
    aws_region: str,
    flow_definition_name: str,
) -> str:
    return (
        f"arn:aws:sagemaker:{aws_region}:{aws_account_id}:flow-definition"
        f"/{flow_definition_name}"
    )


def get_flow_definition_console_url(
    aws_region: str,
    flow_definition_name: str,
) -> str:
    return (
        f"https://console.aws.amazon.com/a2i/home?region={aws_region}#"
        f"/human-review-workflows/{flow_definition_name}"
    )


def parse_flow_definition_name_from_arn(arn: str) -> str:
    """
    Example:

        >>> parse_flow_definition_name_from_arn("arn:aws:sagemaker:us-east-1:111122223333:flow-definition/my-flow")
        'my-flow'
    """
    return arn.split("/")[-1]


def create_flow_definition(
    bsm: BotoSesManager,
    flow_definition_name: str,
    flow_execution_role_arn: str,
    labeling_team_arn: str,
    output_bucket: str,
    output_key: str,
    task_template_name: str,
    task_description: str,
    task_count: int,
    task_availability_life_time_in_seconds: T.Optional[int] = None,
    task_time_limit_in_seconds: T.Optional[int] = None,
    tags: T.Optional[T.Dict[str, str]] = None,
) -> dict:
    """
    ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_flow_definition
    """
    task_template_arn = get_task_template_arn(
        aws_account_id=bsm.aws_account_id,
        aws_region=bsm.aws_region,
        task_template_name=task_template_name,
    )
    if output_key.endswith("/"):
        output_key = output_key[:-1]
    human_loop_config = {
        "WorkteamArn": labeling_team_arn,
        "HumanTaskUiArn": task_template_arn,
        "TaskTitle": task_template_name,
        "TaskDescription": task_description,
        "TaskCount": task_count,
    }
    if task_availability_life_time_in_seconds is not None:
        human_loop_config[
            "TaskAvailabilityLifetimeInSeconds"
        ] = task_availability_life_time_in_seconds
    if task_time_limit_in_seconds is not None:
        human_loop_config["TaskTimeLimitInSeconds"] = task_time_limit_in_seconds
    kwargs = dict(
        FlowDefinitionName=flow_definition_name,
        HumanLoopConfig=human_loop_config,
        OutputConfig={
            "S3OutputPath": f"s3://{output_bucket}/{output_key}",
        },
        RoleArn=flow_execution_role_arn,
    )
    if tags:
        kwargs["Tags"] = to_tag_list(tags)
    response = bsm.sagemaker_client.create_flow_definition(**kwargs)
    return response


def delete_flow_definition(
    bsm: BotoSesManager,
    flow_definition_name: str,
):
    """
    ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition
    """
    return bsm.sagemaker_client.delete_flow_definition(
        FlowDefinitionName=flow_definition_name
    )


# --- High level API
def is_flow_definition_exists(
    bsm: BotoSesManager,
    flow_definition_name: str,
) -> T.Tuple[bool, T.Optional[FlowDefinition]]:
    """
    ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_flow_definition

    :return: tuple of two item, first item is a boolean value, second value is
        the response of ``describe_flow_definition()``, you can call it flow details.
    """
    try:
        response = bsm.sagemaker_client.describe_flow_definition(
            FlowDefinitionName=flow_definition_name
        )
        return True, FlowDefinition.from_describe_flow_definition_response(response)
    except Exception as e:
        if "does not exist" in str(e):
            return False, None
        else:
            raise e


def remove_flow_definition(
    bsm: BotoSesManager,
    flow_definition_name: str,
    wait: bool = True,
    wait_timeout: int = 30,
    verbose: bool = True,
):
    vprint(
        f"{emojis.delete} Remove Human review workflow definition, it may takes 30 sec ~ 1 minute",
        verbose,
    )
    flow_definition_console_url = get_flow_definition_console_url(
        bsm.aws_region,
        flow_definition_name,
    )
    vprint(f"  Preview at {flow_definition_console_url}", verbose)

    is_flow_exists, flow_def = is_flow_definition_exists(
        bsm=bsm,
        flow_definition_name=flow_definition_name,
    )
    if is_flow_exists:
        delete_flow_definition(
            bsm=bsm,
            flow_definition_name=flow_definition_name,
        )
        if wait:
            for _ in Waiter(delays=1, timeout=wait_timeout, indent=2, verbose=verbose):
                is_flow_exists, flow_def = is_flow_definition_exists(
                    bsm=bsm,
                    flow_definition_name=flow_definition_name,
                )
                if is_flow_exists is False:
                    break
                if flow_def.status == "Failed":
                    raise Exception("Failed!")
    else:
        vprint("  Flow definition doesn't exists, do nothing.", verbose)
    vprint(f"  {emojis.succeeded} Successfully delete flow definition {flow_definition_name!r}", verbose)


def deploy_flow_definition(
    bsm: BotoSesManager,
    flow_definition_name: str,
    flow_execution_role_arn: str,
    labeling_team_arn: str,
    output_bucket: str,
    output_key: str,
    task_template_name: str,
    task_description: str,
    task_count: int,
    task_availability_life_time_in_seconds: T.Optional[int] = None,
    task_time_limit_in_seconds: T.Optional[int] = None,
    tags: T.Optional[T.Dict[str, str]] = None,
    wait: bool = True,
    wait_timeout: int = 30,
    verbose: bool = True,
):
    """
    Deploy a Human in Loop workflow. in smart way.
    """
    vprint(
        f"{emojis.deploy} Deploy Human review workflow definition, it may takes 30 sec ~ 1 minute",
        verbose,
    )
    flow_definition_console_url = get_flow_definition_console_url(
        aws_region=bsm.aws_region,
        flow_definition_name=flow_definition_name,
    )
    vprint(f"  preview at {flow_definition_console_url}", verbose)
    is_flow_exists, flow_def = is_flow_definition_exists(
        bsm=bsm,
        flow_definition_name=flow_definition_name,
    )
    if is_flow_exists:
        no_change_flag = (
            (flow_execution_role_arn == flow_def.role_arn)
            and (task_template_name == flow_def.human_loop_config.task_title)
            and (task_description == flow_def.human_loop_config.task_description)
            and (task_count == flow_def.human_loop_config.task_count)
        )
        if task_availability_life_time_in_seconds is not None:
            no_change_flag = no_change_flag and (
                task_availability_life_time_in_seconds
                == flow_def.human_loop_config.task_availability_lifetime_in_seconds
            )
        if task_time_limit_in_seconds is not None:
            no_change_flag = no_change_flag and (
                task_time_limit_in_seconds
                == flow_def.human_loop_config.task_time_limit_in_seconds
            )
        if output_key.endswith("/"):
            output_key = output_key[:-1]
        no_change_flag = no_change_flag and (
            (
                flow_def.output_config.s3_output_path
                == f"s3://{output_bucket}/{output_key}"
            )
        )
        # no need to deploy
        if no_change_flag:
            vprint("  No configuration changed, do nothing.", verbose)
            return
        # remove existing one first
        remove_flow_definition(
            bsm=bsm,
            flow_definition_name=flow_definition_name,
            wait=True,
            verbose=verbose,
        )
    vprint("Create Human review workflow definition ...", verbose)
    create_flow_definition(
        bsm,
        flow_definition_name=flow_definition_name,
        flow_execution_role_arn=flow_execution_role_arn,
        labeling_team_arn=labeling_team_arn,
        output_bucket=output_bucket,
        output_key=output_key,
        task_template_name=task_template_name,
        task_description=task_description,
        task_count=task_count,
        task_availability_life_time_in_seconds=task_availability_life_time_in_seconds,
        task_time_limit_in_seconds=task_time_limit_in_seconds,
        tags=tags,
    )

    if wait:
        for _ in Waiter(delays=1, timeout=wait_timeout, indent=2, verbose=verbose):
            is_flow_exists, flow_def = is_flow_definition_exists(
                bsm=bsm,
                flow_definition_name=flow_definition_name,
            )
            if is_flow_exists is False:
                break
            if flow_def.status == FlowDefinitionStatusEnum.Active.value:
                break
            if flow_def.status == FlowDefinitionStatusEnum.Failed.value:
                raise Exception("Failed")

    vprint(
        f"  {emojis.succeeded} Successfully deployed flow definition {flow_definition_name!r}", verbose
    )
