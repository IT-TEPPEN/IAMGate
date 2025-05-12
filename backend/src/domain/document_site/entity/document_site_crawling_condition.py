from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, timezone


class DocumentSiteCrawlingCondition(BaseModel):
    site_property_id: UUID = Field(description="対象ページのID")
    is_active: bool = Field(default=True, description="この条件が有効かどうか")
    crawl_interval_minutes: int = Field(
        default=1440, description="クローリング間隔（分）"
    )
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @classmethod
    def new(
        cls,
        site_property_id: UUID,
        is_active: bool = True,
        crawl_interval_minutes: int = 1440,
    ) -> "DocumentSiteCrawlingCondition":
        """
        Create a new instance of DocumentSiteCrawlingCondition.

        :param site_property_id: The unique identifier for the document site property.
        :param is_active: Indicates whether the crawling condition is active.
        :param crawl_interval_minutes: The crawling interval in minutes.
        :return: A new instance of DocumentSiteCrawlingCondition.
        """
        return DocumentSiteCrawlingCondition(
            site_property_id=site_property_id,
            is_active=is_active,
            crawl_interval_minutes=crawl_interval_minutes,
        )

    @classmethod
    def reconstruct(
        cls,
        site_property_id: UUID,
        is_active: bool,
        crawl_interval_minutes: int,
        created_at: datetime,
        updated_at: datetime,
    ) -> "DocumentSiteCrawlingCondition":
        """
        Reconstruct an instance of DocumentSiteCrawlingCondition.

        :param site_property_id: The unique identifier for the document site property.
        :param is_active: Indicates whether the crawling condition is active.
        :param crawl_interval_minutes: The crawling interval in minutes.
        :param created_at: The creation timestamp.
        :param updated_at: The last update timestamp.
        :return: An instance of DocumentSiteCrawlingCondition.
        """
        return DocumentSiteCrawlingCondition(
            site_property_id=site_property_id,
            is_active=is_active,
            crawl_interval_minutes=crawl_interval_minutes,
            created_at=created_at,
            updated_at=updated_at,
        )
