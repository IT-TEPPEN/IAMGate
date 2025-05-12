from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from . import dto
from src.domain.document_site.entity import DocumentSiteProperty


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
    def get_actions_list_page_property_crawling(
        self,
    ) -> AbstractContextManager[DocumentSiteProperty | None]:
        """
        Crawl the action list page properties.
        """
        pass
