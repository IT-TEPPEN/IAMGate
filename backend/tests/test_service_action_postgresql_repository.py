"""Service Action PostgreSQL Repository のテスト"""

import pytest
from datetime import datetime, timezone
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.pool import StaticPool

from src.domain.service_action.entity import ServiceAction, EAccessLevel
from src.domain.service_action.value_object import (
    VServiceActionSearchCriteria,
    EActionNameMatch,
    EOrder,
)
from src.infrastructure.service_action.repository import (
    ServiceActionPostgreSQLRepository,
)
from src.infrastructure.service_action.model import MServiceAction


@pytest.fixture
def engine():
    """テスト用のインメモリSQLiteエンジン"""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture
def repository(engine):
    """テスト用リポジトリ"""
    return ServiceActionPostgreSQLRepository(engine)


@pytest.fixture
def sample_action():
    """テスト用サンプルアクション"""
    return ServiceAction.new(
        service_prefix="s3",
        action_name="GetObject",
        action_url="https://docs.aws.amazon.com/s3/latest/userguide/example.html",
        description="Retrieves objects from Amazon S3.",
        access_level=EAccessLevel.Read,
        resource_types=["s3:bucket", "s3:object"],
        condition_keys=["s3:x-amz-server-side-encryption"],
    )


def test_save_and_get_service_action(repository, sample_action):
    """Service Actionの保存と取得のテスト"""
    # 保存
    saved_action = repository.save_service_action(sample_action)
    assert saved_action.id == sample_action.id
    assert saved_action.service_prefix == sample_action.service_prefix
    assert saved_action.action_name == sample_action.action_name

    # 取得
    retrieved_action = repository.get_service_action(sample_action.id)
    assert retrieved_action is not None
    assert retrieved_action.id == sample_action.id
    assert retrieved_action.service_prefix == sample_action.service_prefix
    assert retrieved_action.action_name == sample_action.action_name
    assert retrieved_action.access_level == sample_action.access_level


def test_get_service_action_not_found(repository):
    """存在しないService Actionの取得テスト"""
    result = repository.get_service_action("nonexistent:action")
    assert result is None


def test_save_service_actions_bulk(repository):
    """複数Service Actionの一括保存テスト"""
    actions = [
        ServiceAction.new(
            service_prefix="s3",
            action_name="GetObject",
            action_url="https://docs.aws.amazon.com/s3/latest/userguide/example1.html",
            description="Get an object.",
            access_level=EAccessLevel.Read,
        ),
        ServiceAction.new(
            service_prefix="s3",
            action_name="PutObject",
            action_url="https://docs.aws.amazon.com/s3/latest/userguide/example2.html",
            description="Put an object.",
            access_level=EAccessLevel.Write,
        ),
    ]

    saved_actions = repository.save_service_actions(actions)
    assert len(saved_actions) == 2
    assert saved_actions[0].id == actions[0].id
    assert saved_actions[1].id == actions[1].id


def test_search_service_actions_basic(repository):
    """基本的な検索のテスト"""
    # テストデータを作成
    actions = [
        ServiceAction.new(
            service_prefix="s3",
            action_name="GetObject",
            action_url="https://docs.aws.amazon.com/s3/latest/userguide/example1.html",
            description="Get an object from S3.",
            access_level=EAccessLevel.Read,
        ),
        ServiceAction.new(
            service_prefix="ec2",
            action_name="DescribeInstances",
            action_url="https://docs.aws.amazon.com/ec2/latest/userguide/example.html",
            description="Describe EC2 instances.",
            access_level=EAccessLevel.List,
        ),
    ]
    repository.save_service_actions(actions)

    # 検索条件（すべて取得）
    criteria = VServiceActionSearchCriteria.new()
    results = repository.get_service_actions(criteria)
    assert len(results) == 2


def test_count_service_actions(repository):
    """Service Actionの件数取得テスト"""
    # テストデータを作成
    actions = [
        ServiceAction.new(
            service_prefix="s3",
            action_name="GetObject",
            action_url="https://docs.aws.amazon.com/s3/latest/userguide/example1.html",
            description="Get an object.",
            access_level=EAccessLevel.Read,
        ),
        ServiceAction.new(
            service_prefix="s3",
            action_name="PutObject",
            action_url="https://docs.aws.amazon.com/s3/latest/userguide/example2.html",
            description="Put an object.",
            access_level=EAccessLevel.Write,
        ),
    ]
    repository.save_service_actions(actions)

    # 件数取得
    criteria = VServiceActionSearchCriteria.new()
    count = repository.count_service_actions(criteria)
    assert count == 2


def test_get_last_updated(repository, sample_action):
    """最終更新日時の取得テスト"""
    # 初期状態では None
    last_updated = repository.get_last_updated()
    assert last_updated is None

    # データを保存
    repository.save_service_action(sample_action)

    # 最終更新日時を取得
    last_updated = repository.get_last_updated()
    assert last_updated is not None
    assert isinstance(last_updated, datetime)


def test_update_service_action(repository, sample_action):
    """Service Actionの更新テスト"""
    # 保存
    repository.save_service_action(sample_action)

    # 更新
    updated_action = ServiceAction.reconstruct(
        id=sample_action.id,
        service_prefix=sample_action.service_prefix,
        action_name=sample_action.action_name,
        action_url=sample_action.action_url,
        description="Updated description",
        access_level=EAccessLevel.Write,
        resource_types=sample_action.resource_types,
        condition_keys=sample_action.condition_keys,
        created_at=sample_action.created_at,
        updated_at=datetime.now(timezone.utc),
    )

    result = repository.update_service_action(updated_action)
    assert result.description == "Updated description"
    assert result.access_level == EAccessLevel.Write


def test_delete_service_actions_before(repository):
    """古いService Actionの削除テスト"""
    # 古い日付でデータを作成
    old_date = datetime(2023, 1, 1, tzinfo=timezone.utc)
    actions = [
        ServiceAction.reconstruct(
            id="s3:GetObject",
            service_prefix="s3",
            action_name="GetObject",
            action_url="https://docs.aws.amazon.com/s3/latest/userguide/example.html",
            description="Get an object.",
            access_level="Read",
            resource_types=[],
            condition_keys=[],
            created_at=old_date,
            updated_at=old_date,
        )
    ]
    repository.save_service_actions(actions)

    # 削除（未来の日付を指定）
    future_date = datetime(2024, 1, 1, tzinfo=timezone.utc)
    deleted_count = repository.delete_service_actions_before(future_date)
    assert deleted_count == 1

    # 削除確認
    result = repository.get_service_action("s3:GetObject")
    assert result is None
