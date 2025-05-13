from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from . import dto
from src.domain.document_site.entity import (
    DocumentSiteProperty,
    DocumentSiteCrawlingCondition,
)
from typing import List


class IDocumentSiteUseCase(ABC):
    """
    Abstract base class for document site use cases.
    """

    @abstractmethod
    def get_document_top_site(self) -> dto.ResponseDocumentSiteContent:
        """
        Retrieve the top document site.
        """
        pass

    @abstractmethod
    def update_actions_list_page_properties(
        self, top_page_property: dto.ResponseDocumentSiteContent
    ) -> None:
        """
        Update the properties of the action list pages.
        """
        pass

    @abstractmethod
    def crawl_actions_list_page(
        self, actions_list_page_property: DocumentSiteProperty
    ) -> dto.ResponseDocumentSiteContent:
        """
        Crawl the action list page properties.
        """
        pass

    @abstractmethod
    def get_actions_list_page_property_crawling(
        self,
    ) -> AbstractContextManager[DocumentSiteProperty | None]:
        """
        Crawl the action list page properties.
        """
        pass

    @abstractmethod
    def list_actions_pages(
        self,
    ) -> List[DocumentSiteProperty]:
        """
        Get the action list page properties.
        """
        pass

    @abstractmethod
    def clear_actions_pages(self) -> None:
        """
        Delete the specified document site property.
        """
        pass

    @abstractmethod
    def get_crawling_target(
        self, document_id: str
    ) -> DocumentSiteCrawlingCondition | None:
        """
        Retrieve a crawling target by its ID.
        """
        pass

    @abstractmethod
    def list_crawling_targets(
        self,
    ) -> List[DocumentSiteCrawlingCondition]:
        """
        List all crawling targets.
        """
        pass

    @abstractmethod
    def add_crawling_target(
        self, dto: dto.AddCrawlingTargetRequest
    ) -> DocumentSiteCrawlingCondition:
        """
        Add a crawling target.
        """
        pass

    @abstractmethod
    def delete_crawling_target(self, document_id: str) -> None:
        """
        Delete a crawling target by its ID.
        """
        pass
