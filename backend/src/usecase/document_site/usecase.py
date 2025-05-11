from .i_usecase import IDocumentSiteUseCase
from . import dto, exc

from src.domain.document_site.entity import DocumentSiteProperty, EDocumentType
from src.domain.document_site.repository import IDocumentSiteRepository
from src.domain.document_site.adapter import IDocumentSiteAdapter

from src.domain.share.value_object import VSearchCondition


class DocumentSiteUseCase(IDocumentSiteUseCase):
    """
    Implementation of the document site use case.
    """

    def __init__(
        self,
        document_site_repository: IDocumentSiteRepository,
        document_site_adapter: IDocumentSiteAdapter,
    ) -> None:
        """
        Initialize the DocumentSiteUseCase.

        :param document_site_repository: The document site repository.
        :param document_site_adapter: The document site adapter.
        """
        self.document_site_repository = document_site_repository
        self.document_site_adapter = document_site_adapter

    def get_document_top_site(self):
        """
        Retrieve the top document site.
        """
        # Get the document site properties
        document_site_properties = (
            self.document_site_repository.get_document_site_properties(
                document_type=EDocumentType.トップページ,
                search_condition=VSearchCondition(limit=1),
            )
        )

        if len(document_site_properties) == 0:
            top_document_site_property = DocumentSiteProperty.new(
                document_type=EDocumentType.トップページ,
            )
            self.document_site_repository.save_document_site_property(
                top_document_site_property
            )
        else:
            top_document_site_property = document_site_properties[0]

        # Get the document site content
        document_site_content = self.document_site_adapter.get_document(
            property=top_document_site_property
        )

        if document_site_content is None:
            raise exc.FailToGetContentException(
                f"Document site content not found for\n - property ID: {top_document_site_property.id}\n - URL: {top_document_site_property.url}"
            )

        # Create the response DTO
        response_dto = dto.ResponseDocumentSiteContent(
            id=str(top_document_site_property.id),
            document_type=top_document_site_property.document_type,
            url=top_document_site_property.url,
            description=top_document_site_property.description,
            content=document_site_content.content,
            acquired_at=document_site_content.acquired_at,
        )

        return response_dto

    def update_actions_list_page_properties(self):
        """
        Update the action list page properties.

        :param top_page_property: The top page property.
        """
        document_site_properties = (
            self.document_site_repository.get_document_site_properties(
                document_type=EDocumentType.トップページ,
                search_condition=VSearchCondition(limit=1),
            )
        )

        if len(document_site_properties) == 0:
            top_document_site_property = DocumentSiteProperty.new(
                document_type=EDocumentType.トップページ,
            )
            self.document_site_repository.save_document_site_property(
                top_document_site_property
            )
        else:
            top_document_site_property = document_site_properties[0]

        # Get the action list page properties
        action_list_page_properties = (
            self.document_site_adapter.get_aws_iam_actions_page_properties(
                top_page_property=top_document_site_property
            )
        )

        if len(action_list_page_properties) == 0:
            raise exc.FailToGetContentException(
                f"Action list page properties not found for\n - property ID: {top_document_site_property.id}\n - URL: {top_document_site_property.url}"
            )

        self.document_site_repository.save_document_site_properties(
            action_list_page_properties
        )
