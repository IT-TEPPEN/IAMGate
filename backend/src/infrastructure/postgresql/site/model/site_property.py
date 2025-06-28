from sqlmodel import Field, SQLModel
from sqlalchemy import TEXT, Column
from uuid import UUID
from datetime import datetime


class MSiteProperty(SQLModel, table=True):
    """
    Represents a property of a site.
    """

    id: UUID = Field(primary_key=True)
    document_type: str = Field(sa_column=Column(TEXT))
    description: str = Field(sa_column=Column(TEXT))
    url: str = Field(sa_column=Column(TEXT))
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=False)
