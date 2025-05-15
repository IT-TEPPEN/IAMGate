from abc import ABC, abstractmethod
from typing import List
from ..entity import (
    DocumentSiteProperty,
    DocumentSiteContent,
    EDocumentType,
    DocumentSiteCrawlingCondition,
)
from contextlib import AbstractContextManager

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
    def clear_actions_pages(self) -> None:
        """
        Delete the specified document site property.
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

    @abstractmethod
    def get_crawling_site_condition(
        self, document_id: str
    ) -> DocumentSiteCrawlingCondition | None:
        """
        Retrieve the crawling condition for a document site property.

        :param document_id: The ID of the document site property.
        :return: The crawling condition for the document site property.
        """
        pass

    @abstractmethod
    def list_crawling_site_conditions(
        self,
        document_type: EDocumentType,
        search_condition: VSearchCondition | None = None,
    ) -> list[DocumentSiteCrawlingCondition]:
        """
        Retrieve all crawling conditions for a document site property.

        :return: A list of crawling conditions for the document site property.
        """
        pass

    @abstractmethod
    def save_crawling_site_condition(
        self, document_site_crawling_condition: DocumentSiteCrawlingCondition
    ) -> DocumentSiteCrawlingCondition:
        """
        Save the crawling condition for a document site property.

        :param document_site_crawling_condition: The crawling condition to save.
        :return: The saved crawling condition.
        """
        pass

    @abstractmethod
    def delete_crawling_site_condition(self, document_id: str) -> None:
        """
        Delete the crawling condition for a document site property.

        :param document_id: The ID of the document site property.
        :return: The deleted crawling condition.
        """
        pass

    @abstractmethod
    def pick_and_lock_crawling_target(
        self, num_pick: int = 5
    ) -> AbstractContextManager[DocumentSiteProperty | None]:
        """
        Pick up to `num_pick` crawlable SiteProperty, try to acquire advisory lock for each in order,
        yield the first one that can be locked (or None if none), and auto-release lock after crawling.
        Usage:
            with repo.pick_and_lock_crawling_target(num_pick=5) as site_property:
                if site_property:
                    # do crawling
        """
        pass
