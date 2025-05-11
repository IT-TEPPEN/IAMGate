from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, timezone
from uuid import UUID, uuid4
from enum import Enum


AWS_IAM_ACTIONS_TOP_PAGE_URL = "https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html"
AWS_IAM_ACTIONS_TOP_PAGE_DESCRIPTION = "AWS IAM Actions Top Page"


class EDocumentType(str, Enum):
    """
    Enum for document types
    """

    トップページ = "TOP PAGE"
    アクション一覧ページ = "ACTION PAGE"


class DocumentSiteProperty(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="The unique identifier for the document site property.",
    )
    document_type: EDocumentType
    description: str = Field(
        default="",
        description="The description of the document site property.",
    )
    url: HttpUrl = Field(description="The URL of the document site.")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @classmethod
    def new(
        cls,
        document_type: EDocumentType,
        url: str | None = None,
        description: str | None = None,
    ) -> "DocumentSiteProperty":
        """
        Create a new instance of DocumentSiteProperty.

        :param document_type: The type of the document.
        :param url: The URL of the document site.
        :param description: The description of the document site.
        :return: A new instance of DocumentSiteProperty.
        :raises ValueError: If the document type is not supported or if the URL is not provided for action list pages.

        """
        if document_type == EDocumentType.トップページ:
            if url is None:
                url = AWS_IAM_ACTIONS_TOP_PAGE_URL

            if description is None:
                description = AWS_IAM_ACTIONS_TOP_PAGE_DESCRIPTION

        elif document_type == EDocumentType.アクション一覧ページ:
            if url is None:
                raise ValueError("URL must be provided for action list pages.")

            if description is None:
                description = ""

        return DocumentSiteProperty(
            document_type=document_type,
            url=url,
            description=description,
        )

    @classmethod
    def reconstruct(
        cls,
        id: UUID,
        document_type: EDocumentType,
        url: str,
        description: str,
        created_at: datetime,
        updated_at: datetime,
    ) -> "DocumentSiteProperty":
        """
        Reconstruct an instance of DocumentSiteProperty.

        :param id: The unique identifier for the document site property.
        :param document_type: The type of the document.
        :param url: The URL of the document site.
        :param description: The description of the document site.
        :return: An instance of DocumentSiteProperty.
        """
        return DocumentSiteProperty.model_construct(
            id=id,
            document_type=document_type,
            url=url,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
        )

    def update_url(self, url: str) -> "DocumentSiteProperty":
        """
        Update the URL of the document site property.

        :param url: The new URL of the document site.
        :return: The updated instance of DocumentSiteProperty.
        """
        self.url = url
        self.updated_at = datetime.now(timezone.utc)
        return self

    def update_description(self, description: str) -> "DocumentSiteProperty":
        """
        Update the description of the document site property.

        :param description: The new description of the document site.
        :return: The updated instance of DocumentSiteProperty.
        """
        self.description = description
        self.updated_at = datetime.now(timezone.utc)
        return self


class DocumentSiteContent(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="The unique identifier for the document content.",
    )
    acquired_at: datetime
    content: str = Field(description="The content of the document top page.")

    @classmethod
    def new(
        cls,
        id: UUID,
        content: str,
        acquired_at: datetime | None = None,
    ) -> "DocumentSiteContent":
        """
        Create a new instance of DocumentSiteContent.

        :param id: The unique identifier for the document site property.
        :param content: The content of the document top page.
        :param acquired_at: The date and time when the content was acquired.
        :return: A new instance of DocumentSiteContent.
        """
        if acquired_at is None:
            acquired_at = datetime.now(timezone.utc)

        return DocumentSiteContent(
            id=id,
            content=content,
            acquired_at=acquired_at,
        )

    @classmethod
    def reconstruct(
        cls,
        id: UUID,
        content: str,
        acquired_at: datetime,
    ) -> "DocumentSiteContent":
        """
        Reconstruct an instance of DocumentSiteContent.

        :param id: The unique identifier for the document top page content.
        :param document_id: The unique identifier for the document site property.
        :param content: The content of the document top page.
        :param acquired_at: The date and time when the content was acquired.
        :return: An instance of DocumentSiteContent.
        """
        return DocumentSiteContent.model_construct(
            id=id,
            content=content,
            acquired_at=acquired_at,
        )
