from abc import ABC, abstractmethod
from ..entity import DocumentSiteProperty, DocumentSiteContent


class IDocumentSiteAdapter(ABC):
    """
    Abstract base class for document site adapters.
    """

    @abstractmethod
    def get_document(
        self, property: DocumentSiteProperty
    ) -> DocumentSiteContent | None:
        """
        Retrieve a document site content by its property.

        :param property: The document site property to retrieve the content for.
        :return: The document site content.
        """
        pass

    @abstractmethod
    def get_aws_iam_actions_page_properties(
        self, top_page_property: DocumentSiteProperty
    ) -> list[DocumentSiteProperty]:
        """
        Retrieve a list of AWS IAM action list URLs.

        :param property: The document site property to retrieve the URLs for.
        :return: A list of AWS IAM action list URLs.
        """
        pass

    @abstractmethod
    def extract_service_action_page_properties(
        self, content: DocumentSiteContent
    ) -> list[DocumentSiteProperty]:
        """
        Extract service action page properties from the content.

        :param content: The document site content to extract the properties from.
        :return: A list of service action page properties.
        """
        pass
