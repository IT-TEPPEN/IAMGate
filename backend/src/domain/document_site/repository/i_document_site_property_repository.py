from abc import ABC, abstractmethod
from typing import List
from ..entity import DocumentSiteProperty, DocumentSiteContent, EDocumentType

from src.domain.share.value_object import VSearchCondition


class IDocumentSiteRepository(ABC):
    """
    Abstract base class for document site property repositories.
    """

    @abstractmethod
    def get_document_site_property(
        self, document_id: str
    ) -> DocumentSiteProperty | None:
        """
        Retrieve a document site property by its ID.

        :param document_id: The ID of the document site property to retrieve.
        :return: The document site property.
        """
        pass

    @abstractmethod
    def get_document_site_properties(
        self,
        document_type: EDocumentType,
        search_condition: VSearchCondition | None = None,
    ) -> list[DocumentSiteProperty]:
        """
        Retrieve all document site properties.

        :return: A list of document site properties.
        """
        pass

    @abstractmethod
    def save_document_site_property(
        self, document_site_property: DocumentSiteProperty
    ) -> DocumentSiteProperty:
        """
        Save a document site property.

        :param document_site_property: The document site property to save.
        :return: The saved document site property.
        """
        pass

    @abstractmethod
    def save_document_site_properties(
        self, document_site_properties: List[DocumentSiteProperty]
    ) -> List[DocumentSiteProperty]:
        """
        Save multiple document site properties.

        :param document_site_properties: The list of document site properties to save.
        :return: The saved document site properties.
        """
        pass

    @abstractmethod
    def delete_document_site_property(self, document_id: str) -> None:
        """
        Delete a document site property by its ID.

        :param document_id: The ID of the document site property to delete.
        :return: The deleted document site property.
        """
        pass

    @abstractmethod
    def get_document_site_content(self, document_id: str) -> DocumentSiteContent | None:
        """
        Retrieve a document site content by its ID.

        :param document_id: The ID of the document site content to retrieve.
        :return: The document site content.
        """
        pass

    @abstractmethod
    def save_document_site_content(
        self, document_site_content: DocumentSiteContent
    ) -> DocumentSiteContent:
        """
        Save a document site content.

        :param document_site_content: The document site content to save.
        :return: The saved document site content.
        """
        pass

    @abstractmethod
    def delete_document_site_content(self, document_id: str) -> None:
        """
        Delete a document site content by its ID.

        :param document_id: The ID of the document site content to delete.
        :return: The deleted document site content.
        """
        pass
