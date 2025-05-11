from sqlmodel import Field, Session, SQLModel, select
from sqlalchemy.engine import Engine
from sqlalchemy import text
from ..model import MSiteProperty, MSiteContent
from ..model.site_crawling_condition import MSiteCrawlingCondition

from src.domain.document_site.repository import IDocumentSiteRepository
from src.domain.document_site.entity import (
    DocumentSiteProperty,
    DocumentSiteContent,
    EDocumentType,
)
from src.domain.document_site.entity.document_site_crawling_condition import (
    DocumentSiteCrawlingCondition,
)
from src.domain.share.value_object import VSearchCondition
from contextlib import contextmanager
from typing import Generator


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

    def get_crawling_site_condition(
        self, document_id: str
    ) -> DocumentSiteCrawlingCondition | None:
        """
        Retrieve a crawling site condition by its document ID.

        :param document_id: The ID of the document site property.
        :return: The crawling site condition.
        """
        with Session(self.engine) as session:
            statement = select(MSiteCrawlingCondition).where(
                MSiteCrawlingCondition.site_property_id == document_id
            )
            result = session.exec(statement)
            row = result.first()
            if row is None:
                return None
            return DocumentSiteCrawlingCondition(
                site_property_id=row.site_property_id,
                is_active=getattr(row, "is_active", True),
                force_crawl=row.force_crawl,
                crawl_interval_minutes=row.crawl_interval_minutes,
                created_at=row.created_at,
                updated_at=row.updated_at,
            )

    def list_crawling_site_conditions(
        self,
        document_type: EDocumentType,
        search_condition: VSearchCondition | None = None,
    ) -> list[DocumentSiteCrawlingCondition]:
        """
        List crawling site conditions by document type.

        :param document_type: The type of the document site property.
        :param search_condition: The search condition for pagination.
        :return: A list of crawling site conditions.
        """
        with Session(self.engine) as session:
            # Join MSiteProperty to filter by document_type
            statement = (
                select(MSiteCrawlingCondition)
                .join(
                    MSiteProperty,
                    MSiteCrawlingCondition.site_property_id == MSiteProperty.id,
                )
                .where(MSiteProperty.document_type == document_type.value)
            )
            if search_condition is not None:
                statement = statement.limit(search_condition.limit).offset(
                    search_condition.offset
                )
            result = session.exec(statement)
            rows = result.all()
            return [
                DocumentSiteCrawlingCondition(
                    site_property_id=row.site_property_id,
                    is_active=getattr(row, "is_active", True),
                    force_crawl=row.force_crawl,
                    crawl_interval_minutes=row.crawl_interval_minutes,
                    created_at=row.created_at,
                    updated_at=row.updated_at,
                )
                for row in rows
            ]

    def save_crawling_site_condition(
        self, document_site_crawling_condition: DocumentSiteCrawlingCondition
    ) -> DocumentSiteCrawlingCondition:
        """
        Save a crawling site condition to the database.

        :param document_site_crawling_condition: The crawling site condition to save.
        :return: The saved crawling site condition.
        """
        with Session(self.engine) as session:
            db_obj = MSiteCrawlingCondition(
                site_property_id=document_site_crawling_condition.site_property_id,
                # is_active is not in DB, but included for future-proofing
                force_crawl=document_site_crawling_condition.force_crawl,
                crawl_interval_minutes=document_site_crawling_condition.crawl_interval_minutes,
                created_at=document_site_crawling_condition.created_at,
                updated_at=document_site_crawling_condition.updated_at,
            )
            session.merge(db_obj)
            session.commit()
            return document_site_crawling_condition

    def delete_crawling_site_condition(self, document_id: str) -> None:
        """
        Delete a crawling site condition by its document ID.

        :param document_id: The ID of the document site property.
        """
        with Session(self.engine) as session:
            statement = select(MSiteCrawlingCondition).where(
                MSiteCrawlingCondition.site_property_id == document_id
            )
            result = session.exec(statement)
            row = result.first()
            if row:
                session.delete(row)
                session.commit()

    @contextmanager
    def pick_and_lock_crawling_target(
        self, num_pick: int = 5
    ) -> Generator[DocumentSiteProperty | None, None, None]:
        """
        Pick up to `num_pick` crawlable SiteProperty, try to acquire advisory lock for each in order,
        yield the first one that can be locked (or None if none), and auto-release lock after crawling.
        Usage:
            with repo.pick_and_lock_crawling_target(num_pick=5) as site_property:
                if site_property:
                    # do crawling
        """
        session = None
        lock_id = None
        picked_property = None
        try:
            with Session(self.engine) as s:
                statement = (
                    select(MSiteProperty)
                    .join(
                        MSiteCrawlingCondition,
                        MSiteProperty.id == MSiteCrawlingCondition.site_property_id,
                    )
                    .where(MSiteCrawlingCondition.force_crawl == True)
                    .limit(num_pick)
                )
                result = s.exec(statement)
                site_properties = result.all()
                for prop in site_properties:
                    lock_id_candidate = int(str(prop.id).replace("-", ""), 16) % (2**31)
                    session_candidate = Session(self.engine)
                    lock_result = session_candidate.exec(
                        text("SELECT pg_try_advisory_lock(:id)"),
                        {"id": lock_id_candidate},
                    )
                    lock_result_value = lock_result.first()
                    if lock_result_value and lock_result_value[0]:
                        picked_property = DocumentSiteProperty.reconstruct(
                            id=prop.id,
                            document_type=EDocumentType(prop.document_type),
                            url=prop.url,
                            description=prop.description,
                            created_at=prop.created_at,
                            updated_at=prop.updated_at,
                        )
                        session = session_candidate
                        lock_id = lock_id_candidate
                        break
                    else:
                        session_candidate.close()
            yield picked_property
        finally:
            if session and lock_id is not None:
                session.exec(text("SELECT pg_advisory_unlock(:id)"), {"id": lock_id})
                session.close()

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
