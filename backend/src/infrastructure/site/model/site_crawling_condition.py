from sqlmodel import Field, SQLModel
from uuid import UUID
from datetime import datetime, timezone


class MSiteCrawlingCondition(SQLModel, table=True):
    """
    Represents crawling condition for a site property.
    """

    site_property_id: UUID = Field(primary_key=True, foreign_key="msiteproperty.id")
    should_crawl: bool = Field(nullable=False)
    force_crawl: bool = Field(nullable=False)
    crawl_interval_minutes: int = Field(nullable=False)
    created_at: datetime = Field(
        nullable=False,
    )
    updated_at: datetime = Field(
        nullable=False,
    )
