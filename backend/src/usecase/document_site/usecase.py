from .i_usecase import IDocumentSiteUseCase
from . import dto, exc
from datetime import datetime, timedelta, timezone

from src.domain.document_site.entity import (
    DocumentSiteProperty,
    EDocumentType,
    DocumentSiteCrawlingCondition,
)
from src.domain.document_site.repository import IDocumentSiteRepository
from src.domain.document_site.adapter import IDocumentSiteAdapter
from src.domain.service_action.adapter import IServiceActionAdapter

from src.domain.share.value_object import VSearchCondition


class DocumentSiteUseCase(IDocumentSiteUseCase):
    """
    Implementation of the document site use case.
    """

    def __init__(
        self,
        document_site_repository: IDocumentSiteRepository,
        document_site_adapter: IDocumentSiteAdapter,
        service_action_adapter: IServiceActionAdapter,
    ) -> None:
        """
        Initialize the DocumentSiteUseCase.

        :param document_site_repository: The document site repository.
        :param document_site_adapter: The document site adapter.
        :param service_action_adapter: The service action adapter.
        """
        self.document_site_repository = document_site_repository
        self.document_site_adapter = document_site_adapter
        self.service_action_adapter = service_action_adapter

    def get_document_top_site(self):
        """
        Retrieve the top document site.
        """
        # Get the document site properties
        document_site_properties = self.document_site_repository.get_document_site_properties(
            document_type=EDocumentType.トップページ,
            # search_condition=VSearchCondition(limit=1),
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

    def update_actions_list_page_properties(self, interval_minutes=1440):
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

        # Get the document site content
        top_document_site_content = (
            self.document_site_repository.get_document_site_content(
                document_id=top_document_site_property.id
            )
        )

        if top_document_site_content is not None:
            # Check if the content is older than the interval
            if top_document_site_content.acquired_at > datetime.now(
                tz=timezone.utc
            ) - timedelta(minutes=interval_minutes):
                print(
                    f"[INFO] Document site content is up to date. Skipping update.\n - URL: {top_document_site_property.url}"
                )
                return

        document_site_content = self.document_site_adapter.get_document(
            property=top_document_site_property
        )

        if document_site_content is None:
            raise exc.FailToGetContentException(
                f"Document site content not found for\n - property ID: {str(top_document_site_property.id)}\n - URL: {top_document_site_property.url}"
            )

        # Save the document site content
        self.document_site_repository.save_document_site_content(
            document_site_content=document_site_content,
        )

        # Get the action list page properties
        action_list_page_properties = (
            self.document_site_adapter.extract_service_action_page_properties(
                content=document_site_content
            )
        )

        existing_action_list_page_properties = (
            self.document_site_repository.get_document_site_properties(
                document_type=EDocumentType.アクション一覧ページ,
            )
        )
        existing_action_list_page_urls = [
            str(existing_action_list_page_property.url)
            for existing_action_list_page_property in existing_action_list_page_properties
        ]

        additional_action_list_page_properties = [
            action_list_page_property
            for action_list_page_property in action_list_page_properties
            if str(action_list_page_property.url) not in existing_action_list_page_urls
        ]

        if len(additional_action_list_page_properties) == 0:
            print("[INFO] No action list page properties found. Skipping update.")

        self.document_site_repository.save_document_site_properties(
            additional_action_list_page_properties
        )

    def crawl_actions_list_page(self, actions_list_page_property):
        """
        Crawl the action list page.

        :param actions_list_page_property: The action list page property.
        """
        # Get the document site content
        document_site_content = self.document_site_adapter.get_document(
            property=actions_list_page_property
        )

        if document_site_content is None:
            raise exc.FailToGetContentException(
                f"Document site content not found for\n - property ID: {str(actions_list_page_property.id)}\n - URL: {actions_list_page_property.url}"
            )

        # Save the document site content
        self.document_site_repository.save_document_site_content(
            document_site_content=document_site_content,
        )

        # Create the response DTO
        response_dto = dto.ResponseDocumentSiteContent(
            id=str(actions_list_page_property.id),
            url=actions_list_page_property.url,
            description=actions_list_page_property.description,
            content=document_site_content.content,
            acquired_at=document_site_content.acquired_at,
        )

        return response_dto

    def get_actions_list_page_property_crawling(self):
        """
        Crawl the action list page properties.

        :param top_page_property: The top page property.
        """
        return self.document_site_repository.pick_and_lock_crawling_target(5)

    def list_actions_pages(self):
        """
        Get the action list page properties.
        """
        action_list_page_properties = (
            self.document_site_repository.get_document_site_properties(
                document_type=EDocumentType.アクション一覧ページ,
            )
        )

        return action_list_page_properties

    def clear_actions_pages(self):
        """
        Delete all document site properties.
        """
        self.document_site_repository.clear_actions_pages()

    def get_crawling_target(self, document_id):
        """
        Retrieve a crawling target by its ID.

        :param document_id: The ID of the document site property.
        :return: The crawling target.
        """
        # Get the crawling condition
        crawling_condition = self.document_site_repository.get_crawling_site_condition(
            document_id=document_id
        )

        return crawling_condition

    def list_crawling_targets(self):
        """
        List all crawling targets.
        :return: A list of crawling targets.
        """
        crawling_targets = self.document_site_repository.list_crawling_site_conditions(
            EDocumentType.アクション一覧ページ
        )

        return crawling_targets

    def add_crawling_target(self, dto):
        """
        Add a crawling target.

        :param dto: The document site property to add.
        """
        crawling_condition = DocumentSiteCrawlingCondition.new(
            dto.site_id, crawl_interval_minutes=dto.crawl_interval
        )

        # Save the crawling condition
        self.document_site_repository.save_crawling_site_condition(crawling_condition)

        return crawling_condition

    def delete_crawling_target(self, document_id):
        """
        Delete a crawling target by its ID.

        :param document_id: The ID of the document site property.
        """
        # Delete the crawling condition
        self.document_site_repository.delete_crawling_site_condition(document_id)

    def get_service_actions_from_content(self, content):
        """
        Get service actions from the content.

        :param content: The document site content.
        """
        # Get the service actions
        service_actions = (
            self.service_action_adapter.extract_service_actions_from_content(
                content=content
            )
        )

        return service_actions
