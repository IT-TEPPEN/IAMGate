from pydantic import BaseModel
from .action import ServiceAction


class ServiceActions(BaseModel):
    """
    Class representing a collection of service actions.
    """

    # Service Prefix
    id: str
    service_name: str
    service_actions: list[ServiceAction]

    @classmethod
    def new(
        cls,
        service_prefix: str,
        service_name: str,
        service_actions: list[ServiceAction],
    ) -> "ServiceActions":
        """
        Create a new instance of ServiceActions.

        :param id: The unique identifier for the service actions.
        :param service_name: The name of the service.
        :param service_actions: A list of ServiceAction instances.
        :return: An instance of ServiceActions.
        """
        return ServiceActions(
            id=service_prefix,
            service_name=service_name,
            service_actions=service_actions,
        )

    @classmethod
    def reconstruct(
        cls,
        id: str,
        service_name: str,
        service_actions: list[ServiceAction],
    ) -> "ServiceActions":
        """
        Reconstruct an instance of ServiceActions.

        :param id: The unique identifier for the service actions.
        :param service_name: The name of the service.
        :param service_actions: A list of ServiceAction instances.
        :return: An instance of ServiceActions.
        """
        return ServiceActions(
            id=id,
            service_name=service_name,
            service_actions=service_actions,
        )
