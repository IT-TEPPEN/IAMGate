from abc import ABC, abstractmethod
from . import dto


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
