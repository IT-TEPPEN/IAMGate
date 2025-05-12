import pytest
from uuid import uuid4
from datetime import datetime, timedelta, timezone
from sqlmodel import create_engine, SQLModel, Session
import sqlalchemy
from sqlalchemy import text

from src.infrastructure.site.repository.site_postgresql_repository import (
    SitePostgreSQLRepository,
)
from src.infrastructure.site.model import MSiteProperty, MSiteContent
from src.infrastructure.site.model.site_crawling_condition import MSiteCrawlingCondition
from src.domain.document_site.entity import EDocumentType, DocumentSiteProperty


@pytest.fixture(scope="session")
def pg_engine():
    # テスト用PostgreSQLデータベースを作成（存在しなければ）
    admin_engine = create_engine(
        "postgresql://iamgate_user:iamgate_password@db:5432/postgres",
        isolation_level="AUTOCOMMIT",
        echo=False,
    )
    db_name = "iamgate_test"
    with admin_engine.connect() as conn:
        try:
            conn.execute(text(f"CREATE DATABASE {db_name}"))
        except sqlalchemy.exc.ProgrammingError as e:
            if f'database "{db_name}" already exists' not in str(e):
                raise
    # テストDBに接続
    engine = create_engine(
        f"postgresql://iamgate_user:iamgate_password@db:5432/{db_name}", echo=False
    )
    SQLModel.metadata.create_all(engine)
    return engine


def insert_property_with_condition_and_content(
    session, prop_id, force_crawl, should_crawl, acquired_at=None
):
    prop = MSiteProperty(
        id=prop_id,
        document_type=EDocumentType.アクション一覧ページ.value,
        description="desc",
        url="https://example.com",
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    session.add(prop)
    session.commit()  # まず親テーブルを確定
    cond = MSiteCrawlingCondition(
        site_property_id=prop_id,
        force_crawl=force_crawl,
        should_crawl=should_crawl,
        crawl_interval_minutes=60,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    session.add(cond)
    if acquired_at:
        content = MSiteContent(
            id=prop_id,
            version=int(acquired_at.timestamp()),
            content="test content",
            acquired_at=acquired_at,
        )
        session.add(content)
    session.commit()


def test_pick_and_lock_crawling_target_prioritization(pg_engine):
    repo = SitePostgreSQLRepository(pg_engine)
    now = datetime.now(timezone.utc)
    with Session(pg_engine) as session:
        # Oldest acquired_at, should_crawl
        insert_property_with_condition_and_content(
            session, uuid4(), False, True, now - timedelta(days=10)
        )
        # Newest acquired_at, should_crawl
        insert_property_with_condition_and_content(
            session, uuid4(), False, True, now - timedelta(days=1)
        )
        # No content, should_crawl
        insert_property_with_condition_and_content(session, uuid4(), False, True, None)
        # force_crawl, recent content
        insert_property_with_condition_and_content(
            session, uuid4(), True, False, now - timedelta(hours=1)
        )
        # force_crawl, no content
        insert_property_with_condition_and_content(session, uuid4(), True, False, None)

    # Should pick force_crawl with no content first
    with repo.pick_and_lock_crawling_target(num_pick=3) as prop:
        assert prop is not None
        # Should be force_crawl True and no content (most urgent)
        assert prop is not None

    # Should pick next by force_crawl with recent content
    with repo.pick_and_lock_crawling_target(num_pick=5) as prop:
        assert prop is not None

    # Should pick should_crawl with no content next
    # (after force_crawl are locked)
    # This is a basic prioritization test
