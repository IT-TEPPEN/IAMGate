from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, timezone
from typing import Optional


class EAccessLevel(str, Enum):
    """
    List:
    Read:
    Write:
    Permissions management:
    Tagging:
    """

    リスト = "List"
    読み込み = "Read"
    書き込み = "Write"
    権限管理 = "Permissions management"
    タグ付け = "Tagging"


class ServiceAction(BaseModel):
    id: str
    service_prefix: str
    service_name: str
    action_name: str
    action_url: str
    description: str
    access_level: EAccessLevel
    resource_types: list[str] = Field(default_factory=list)
    condition_keys: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @classmethod
    def new(
        cls,
        service_prefix: str,
        service_name: str,
        action_name: str,
        action_url: str,
        description: str,
        access_level: str,
        resource_types: Optional[list[str]] = None,
        condition_keys: Optional[list[str]] = None,
    ) -> "ServiceAction":
        """
        Create a new instance of ServiceAction.

        :param service_prefix: The prefix of the service (e.g., 's3', 'ec2').
        :param service_name: The official name of the service (e.g., 'Amazon S3', 'Amazon EC2').
        :param action_name: The name of the action.
        :param action_url: The URL of the action.
        :param description: The description of the action.
        :param access_level: The access level of the action.
        :param resource_types: The resource types for the action.
        :param condition_keys: The condition keys for the action.
        :return: An instance of ServiceAction.
        """
        return ServiceAction(
            id=f"{service_prefix}:{action_name}",
            service_prefix=service_prefix,
            service_name=service_name,
            action_name=action_name,
            action_url=action_url,
            description=description,
            access_level=EAccessLevel(access_level),
            resource_types=resource_types or [],
            condition_keys=condition_keys or [],
        )

    @classmethod
    def reconstruct(
        cls,
        id: str,
        service_prefix: str,
        service_name: str,
        action_name: str,
        action_url: str,
        description: str,
        access_level: str,
        resource_types: Optional[list[str]] = None,
        condition_keys: Optional[list[str]] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> "ServiceAction":
        """
        Reconstruct an instance of ServiceAction.

        :param id: The unique identifier for the service action.
        :param service_prefix: The prefix of the service (e.g., 's3', 'ec2').
        :param service_name: The official name of the service (e.g., 'Amazon S3', 'Amazon EC2').
        :param action_name: The name of the action.
        :param action_url: The URL of the action.
        :param description: The description of the action.
        :param access_level: The access level of the action.
        :param resource_types: The resource types for the action.
        :param condition_keys: The condition keys for the action.
        :param created_at: The creation timestamp.
        :param updated_at: The update timestamp.
        :return: An instance of ServiceAction.
        """
        now = datetime.now(timezone.utc)
        return ServiceAction(
            id=id,
            service_prefix=service_prefix,
            service_name=service_name,
            action_name=action_name,
            action_url=action_url,
            description=description,
            access_level=EAccessLevel(access_level),
            resource_types=resource_types or [],
            condition_keys=condition_keys or [],
            created_at=created_at or now,
            updated_at=updated_at or now,
        )
