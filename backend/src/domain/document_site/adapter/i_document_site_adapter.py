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
