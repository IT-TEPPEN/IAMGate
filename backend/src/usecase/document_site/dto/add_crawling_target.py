from pydantic import BaseModel, Field


class AddCrawlingTargetRequest(BaseModel):
    """
    Request model for adding a crawling target.
    """

    site_id: str
    """
    The ID of the site to which the crawling target belongs.
    """

    crawl_interval: int = Field(
        default=1440,
        ge=10,
        description="The interval between crawls, in minutes.",
    )
    """
    The interval between crawls, in minutes.
    """
