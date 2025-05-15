from pydantic import BaseModel
from enum import Enum


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
    action_name: str
    action_url: str
    description: str
    access_level: EAccessLevel

    @classmethod
    def new(
        cls,
        service_prefix: str,
        action_name: str,
        action_url: str,
        description: str,
        access_level: str,
    ) -> "ServiceAction":
        """
        Create a new instance of ServiceAction.

        :param service_prefix: The prefix of the service.
        :param action_name: The name of the action.
        :param action_url: The URL of the action.
        :param description: The description of the action.
        :param access_level: The access level of the action.
        :return: An instance of ServiceAction.
        """
        return ServiceAction(
            id=f"{service_prefix}:{action_name}",
            service_prefix=service_prefix,
            action_name=action_name,
            action_url=action_url,
            description=description,
            access_level=access_level,
        )

    @classmethod
    def reconstruct(
        cls,
        id: str,
        service_prefix: str,
        action_name: str,
        action_url: str,
        description: str,
        access_level: str,
    ) -> "ServiceAction":
        """
        Reconstruct an instance of ServiceAction.

        :param id: The unique identifier for the service action.
        :param service_prefix: The prefix of the service.
        :param action_name: The name of the action.
        :param action_url: The URL of the action.
        :param description: The description of the action.
        :param access_level: The access level of the action.
        :return: An instance of ServiceAction.
        """
        return ServiceAction(
            id=id,
            service_prefix=service_prefix,
            action_name=action_name,
            action_url=action_url,
            description=description,
            access_level=access_level,
        )
