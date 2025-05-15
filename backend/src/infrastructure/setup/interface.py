from src.domain.document_site.adapter import IDocumentSiteAdapter
from src.domain.document_site.repository import IDocumentSiteRepository
from src.domain.service_action.adapter import IServiceActionAdapter


class Infrastructure:
    """
    Infrastructure layer for the application.
    """

    def __init__(
        self,
        document_site_repository: IDocumentSiteRepository,
        document_site_adapter: IDocumentSiteAdapter,
        service_action_adapter: IServiceActionAdapter,
    ) -> None:
        """
        Initialize the Infrastructure layer.

        :param document_site_repository: The document site repository.
        :param document_site_adapter: The document site adapter.
        """
        self.document_site_repository = document_site_repository
        self.document_site_adapter = document_site_adapter
        self.service_action_adapter = service_action_adapter
