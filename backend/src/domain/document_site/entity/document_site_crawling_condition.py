from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, timezone


class DocumentSiteCrawlingCondition(BaseModel):
    site_property_id: UUID = Field(description="対象ページのID")
    is_active: bool = Field(default=True, description="この条件が有効かどうか")
    force_crawl: bool = Field(default=False, description="即時クローリングか")
    crawl_interval_minutes: int = Field(
        default=1440, description="クローリング間隔（分）"
    )
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
