from pydantic import BaseModel
from datetime import datetime


class ResponseDocumentSiteContent(BaseModel):
    """
    Response model for Document Site Content.
    """

    id: str
    url: str
    description: str
    content: str
    acquired_at: datetime
