from sqlmodel import Field, SQLModel
from sqlalchemy import TEXT, Column
from uuid import UUID
from datetime import datetime

from src.domain.document_site.entity import DocumentSiteContent


class MSiteContent(SQLModel, table=True):
    """
    Represents the content of a site.
    """

    id: UUID = Field(primary_key=True)
    version: int = Field(primary_key=True)
    content: str = Field(sa_column=Column(TEXT))
    acquired_at: datetime = Field(nullable=False)

    @classmethod
    def new(
        cls,
        site_content: DocumentSiteContent,
    ) -> "MSiteContent":
        """
        Create a new instance of MSiteContent.

        :param site_content: The content of the document top page.
        :return: A new instance of MSiteContent.
        """
        return MSiteContent(
            id=site_content.id,
            version=int(site_content.acquired_at.timestamp()),
            content=site_content.content,
            acquired_at=site_content.acquired_at,
        )

    def to_entity(self) -> DocumentSiteContent:
        """
        Convert the MSiteContent instance to a DocumentSiteContent entity.

        :return: A DocumentSiteContent entity.
        """
        return DocumentSiteContent.reconstruct(
            id=self.id,
            content=self.content,
            acquired_at=self.acquired_at,
        )
