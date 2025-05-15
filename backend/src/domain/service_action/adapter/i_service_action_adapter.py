from abc import ABC, abstractmethod
from ..entity import ServiceActions


class IServiceActionAdapter(ABC):
    """
    Abstract base class for service action adapters.
    """

    @abstractmethod
    def get_service_actions(self, url: str) -> ServiceActions:
        """
        Retrieve service actions from the given URL.
        :param url: The URL to retrieve service actions from.
        :return: A list of service actions.
        """

        pass

    @abstractmethod
    def extract_service_actions_from_content(
        self, content: str
    ) -> list[ServiceActions]:
        """
        Extract service action page properties from the content.
        :param content: The document site content.
        :return: A list of service action page properties.
        """
        pass
