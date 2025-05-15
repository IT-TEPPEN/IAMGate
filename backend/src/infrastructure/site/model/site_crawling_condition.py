from sqlmodel import Field, SQLModel
from uuid import UUID
from datetime import datetime, timezone

from src.domain.document_site.entity import DocumentSiteCrawlingCondition


class MSiteCrawlingCondition(SQLModel, table=True):
    """
    Represents crawling condition for a site property.
    """

    site_property_id: UUID = Field(primary_key=True, foreign_key="msiteproperty.id")
    is_active: bool = Field(nullable=False)
    crawl_interval_minutes: int = Field(nullable=False)
    created_at: datetime = Field(
        nullable=False,
    )
    updated_at: datetime = Field(
        nullable=False,
    )

    @classmethod
    def from_entity(
        cls,
        site_crawling_condition: DocumentSiteCrawlingCondition,
    ) -> "MSiteCrawlingCondition":
        """
        Create a new instance of MSiteCrawlingCondition.

        :param site_crawling_condition: The crawling condition for the site property.
        :return: A new instance of MSiteCrawlingCondition.
        """
        return MSiteCrawlingCondition(
            site_property_id=site_crawling_condition.site_property_id,
            is_active=site_crawling_condition.is_active,
            crawl_interval_minutes=site_crawling_condition.crawl_interval_minutes,
            created_at=site_crawling_condition.created_at,
            updated_at=site_crawling_condition.updated_at,
        )

    def to_entity(self) -> DocumentSiteCrawlingCondition:
        """
        Convert the MSiteCrawlingCondition instance to a DocumentSiteCrawlingCondition entity.

        :return: A DocumentSiteCrawlingCondition entity.
        """
        return DocumentSiteCrawlingCondition.reconstruct(
            site_property_id=self.site_property_id,
            is_active=self.is_active,
            crawl_interval_minutes=self.crawl_interval_minutes,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
