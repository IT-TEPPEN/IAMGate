from sqlmodel import Field, Session, SQLModel, select
from sqlalchemy.engine import Engine
from ..model import MSiteProperty, MSiteContent

from src.domain.document_site.repository import IDocumentSiteRepository
from src.domain.document_site.entity import (
    DocumentSiteProperty,
    DocumentSiteContent,
    EDocumentType,
)

from src.domain.share.value_object import VSearchCondition


class SitePostgreSQLRepository(IDocumentSiteRepository):
    """
    PostgreSQL implementation of the DocumentSiteRepository.
    """

    def __init__(self, engine: Engine) -> None:
        """
        Initialize the SitePostgreSQLRepository.

        :param engine: The SQLAlchemy engine.
        """
        self.engine = engine

    def get_document_site_property(self, document_id):
        """
        Retrieve a document site property by its ID.

        :param document_id: The ID of the document site property.
        :return: The document site property.
        """
        with Session(self.engine) as session:
            statement = select(MSiteProperty).where(MSiteProperty.id == document_id)
            result = session.exec(statement)
            document_site_property = result.first()
            if document_site_property is None:
                return None

            return DocumentSiteProperty.reconstruct(
                id=document_site_property.id,
                document_type=EDocumentType(document_site_property.document_type),
                url=document_site_property.url,
                description=document_site_property.description,
                created_at=document_site_property.created_at,
                updated_at=document_site_property.updated_at,
            )

    def get_document_site_properties(self, document_type, search_condition=None):
        """
        Retrieve document site properties by their type.

        :param document_type: The type of the document site property.
        :param search_condition: The search condition for pagination.
        :return: A list of document site properties.
        """
        with Session(self.engine) as session:
            statement = select(MSiteProperty).where(
                MSiteProperty.document_type == document_type.value
            )
            if search_condition is not None:
                statement = self.__add_condition_statement_to_SiteProperty(
                    statement, search_condition
                )

            result = session.exec(statement)
            document_site_properties = result.all()

            return [
                DocumentSiteProperty.reconstruct(
                    id=document_site_property.id,
                    document_type=EDocumentType(document_site_property.document_type),
                    url=document_site_property.url,
                    description=document_site_property.description,
                    created_at=document_site_property.created_at,
                    updated_at=document_site_property.updated_at,
                )
                for document_site_property in document_site_properties
            ]

    def save_document_site_property(self, document_site_property):
        """
        Save a document site property to the database.

        :param document_site_property: The document site property to save.
        """
        with Session(self.engine) as session:
            session.add(
                MSiteProperty(
                    id=document_site_property.id,
                    document_type=document_site_property.document_type.value,
                    url=str(document_site_property.url),
                    description=document_site_property.description,
                    created_at=document_site_property.created_at,
                    updated_at=document_site_property.updated_at,
                )
            )
            session.commit()

    def save_document_site_properties(self, document_site_properties):
        """
        Save multiple document site properties to the database.

        :param document_site_properties: The list of document site properties to save.
        """
        with Session(self.engine) as session:
            for document_site_property in document_site_properties:
                session.add(
                    MSiteProperty(
                        id=document_site_property.id,
                        document_type=document_site_property.document_type.value,
                        url=str(document_site_property.url),
                        description=document_site_property.description,
                        created_at=document_site_property.created_at,
                        updated_at=document_site_property.updated_at,
                    )
                )
            session.commit()

    def delete_document_site_property(self, document_id):
        """
        Delete a document site property by its ID.

        :param document_id: The ID of the document site property to delete.
        """
        with Session(self.engine) as session:
            statement = select(MSiteProperty).where(MSiteProperty.id == document_id)
            result = session.exec(statement)
            document_site_property = result.first()
            if document_site_property is None:
                return

            session.delete(document_site_property)
            session.commit()

    def get_document_site_content(self, document_id):
        """
        Retrieve a document site content by its ID.

        :param document_id: The ID of the document site content.
        :return: The document site content.
        """
        with Session(self.engine) as session:
            statement = (
                select(MSiteContent)
                .where(MSiteContent.id == document_id)
                .order_by(MSiteContent.version.desc())
                .limit(1)
            )
            result = session.exec(statement)
            document_site_content = result.first()
            if document_site_content is None:
                return None

            return DocumentSiteContent.reconstruct(
                id=document_site_content.id,
                content=document_site_content.content,
                acquired_at=document_site_content.acquired_at,
            )

    def save_document_site_content(self, document_site_content):
        """
        Save a document site content to the database.

        :param document_site_content: The document site content to save.
        """
        with Session(self.engine) as session:
            session.add(
                MSiteContent.new(
                    site_content=document_site_content,
                )
            )
            session.commit()

    def delete_document_site_content(self, document_id):
        """
        Delete a document site content by its ID.

        :param document_id: The ID of the document site content to delete.
        """
        with Session(self.engine) as session:
            statement = select(MSiteContent).where(
                MSiteContent.id == document_id,
            )
            result = session.exec(statement)
            document_site_content = result.first()
            if document_site_content is None:
                return

            session.delete(document_site_content)
            session.commit()

    def __add_condition_statement_to_SiteProperty(
        self, statement, search_condition: VSearchCondition
    ):
        """
        Add conditions to the SQL statement based on the search condition.

        :param statement: The SQL statement.
        :param search_condition: The search condition.
        :return: The modified SQL statement.
        """
        statement = statement.limit(search_condition.limit)
        statement = statement.offset(search_condition.offset)

        if search_condition.sort_by == "id":
            if search_condition.order == "asc":
                statement = statement.order_by(MSiteProperty.id.asc())
            else:
                statement = statement.order_by(MSiteProperty.id.desc())
        elif search_condition.sort_by == "document_type":
            if search_condition.order == "asc":
                statement = statement.order_by(MSiteProperty.document_type.asc())
            else:
                statement = statement.order_by(MSiteProperty.document_type.desc())
        elif search_condition.sort_by == "url":
            if search_condition.order == "asc":
                statement = statement.order_by(MSiteProperty.url.asc())
            else:
                statement = statement.order_by(MSiteProperty.url.desc())
        elif search_condition.sort_by == "description":
            if search_condition.order == "asc":
                statement = statement.order_by(MSiteProperty.description.asc())
            else:
                statement = statement.order_by(MSiteProperty.description.desc())
        elif search_condition.sort_by == "created_at":
            if search_condition.order == "asc":
                statement = statement.order_by(MSiteProperty.created_at.asc())
            else:
                statement = statement.order_by(MSiteProperty.created_at.desc())
        elif search_condition.sort_by == "updated_at":
            if search_condition.order == "asc":
                statement = statement.order_by(MSiteProperty.updated_at.asc())
            else:
                statement = statement.order_by(MSiteProperty.updated_at.desc())

        return statement
