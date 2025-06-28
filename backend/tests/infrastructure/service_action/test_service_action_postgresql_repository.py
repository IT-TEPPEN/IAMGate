import pytest
from datetime import datetime, timezone
from sqlmodel import SQLModel, create_engine, Session, select
from sqlalchemy import Engine
from typing import Generator

from src.domain.service_action.entity import ServiceAction, EAccessLevel
from src.domain.service_action.value_object import VServiceActionSearchCriteria, EActionNameMatch, EOrder
from src.infrastructure.service_action.repository import ServiceActionPostgreSQLRepository
from src.infrastructure.service_action.model import MServiceAction


# テスト用の PostgreSQL データベース URL
TEST_DATABASE_URL = "postgresql://test:test@localhost:5433/test_iamgate"


@pytest.fixture(scope="session")
def engine() -> Generator[Engine, None, None]:
    """テスト用のPostgreSQLエンジンを作成"""
    engine = create_engine(TEST_DATABASE_URL, echo=True)
    
    # テーブル作成
    SQLModel.metadata.create_all(engine)
    
    yield engine
    
    # テスト後にテーブルを削除
    SQLModel.metadata.drop_all(engine)


@pytest.fixture
def repository(engine: Engine) -> ServiceActionPostgreSQLRepository:
    """テスト用のリポジトリインスタンスを作成"""
    return ServiceActionPostgreSQLRepository(engine)


@pytest.fixture(autouse=True)
def clean_database(engine: Engine):
    """各テスト前にデータベースをクリーンアップ"""
    with Session(engine) as session:
        # 全レコードを削除
        result = session.exec(select(MServiceAction))
        for action in result:
            session.delete(action)
        session.commit()


@pytest.fixture
def sample_service_action() -> ServiceAction:
    """テスト用のServiceActionを作成"""
    return ServiceAction.new(
        service_prefix="s3",
        action_name="GetObject",
        action_url="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html",
        description="Retrieves objects from Amazon S3",
        access_level=EAccessLevel.読み込み,
        resource_types=["object"],
        condition_keys=["s3:ExistingObjectTag/<key>"]
    )


class TestServiceActionPostgreSQLRepository:
    """ServiceActionPostgreSQLRepositoryのテストクラス"""

    def test_save_and_get_service_action(self, repository: ServiceActionPostgreSQLRepository, sample_service_action: ServiceAction):
        """Service Actionの保存と取得をテスト"""
        # 保存
        saved_action = repository.save_service_action(sample_service_action)
        
        # 基本的な検証
        assert saved_action.id == "s3:GetObject"
        assert saved_action.service_prefix == "s3"
        assert saved_action.action_name == "GetObject"
        assert saved_action.access_level == EAccessLevel.読み込み
        
        # 取得
        retrieved_action = repository.get_service_action("s3:GetObject")
        
        assert retrieved_action is not None
        assert retrieved_action.id == saved_action.id
        assert retrieved_action.service_prefix == saved_action.service_prefix
        assert retrieved_action.action_name == saved_action.action_name
        assert retrieved_action.description == saved_action.description
        assert retrieved_action.access_level == saved_action.access_level
        assert retrieved_action.resource_types == saved_action.resource_types
        assert retrieved_action.condition_keys == saved_action.condition_keys

    def test_get_service_action_not_found(self, repository: ServiceActionPostgreSQLRepository):
        """存在しないService Actionの取得をテスト"""
        result = repository.get_service_action("nonexistent:action")
        assert result is None

    def test_save_service_actions_bulk(self, repository: ServiceActionPostgreSQLRepository):
        """複数のService Actionの一括保存をテスト"""
        actions = [
            ServiceAction.new(
                service_prefix="s3",
                action_name="GetObject",
                action_url="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html",
                description="Retrieves objects from Amazon S3",
                access_level=EAccessLevel.読み込み,
            ),
            ServiceAction.new(
                service_prefix="s3",
                action_name="PutObject",
                action_url="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html",
                description="Adds an object to a bucket",
                access_level=EAccessLevel.書き込み,
            ),
        ]
        
        # 一括保存
        saved_actions = repository.save_service_actions(actions)
        
        assert len(saved_actions) == 2
        assert all(action.id is not None for action in saved_actions)
        
        # 個別に取得して確認
        action1 = repository.get_service_action("s3:GetObject")
        action2 = repository.get_service_action("s3:PutObject")
        
        assert action1 is not None
        assert action2 is not None
        assert action1.access_level == EAccessLevel.読み込み
        assert action2.access_level == EAccessLevel.書き込み

    def test_update_service_action(self, repository: ServiceActionPostgreSQLRepository, sample_service_action: ServiceAction):
        """Service Actionの更新をテスト"""
        # 保存
        saved_action = repository.save_service_action(sample_service_action)
        
        # 更新用のアクションを作成
        updated_action = ServiceAction.reconstruct(
            id=saved_action.id,
            service_prefix=saved_action.service_prefix,
            action_name=saved_action.action_name,
            action_url=saved_action.action_url,
            description="Updated description",
            access_level=EAccessLevel.書き込み,  # 変更
            resource_types=["object", "bucket"],  # 変更
            condition_keys=["s3:ExistingObjectTag/<key>", "s3:RequestedRegion"],  # 変更
            created_at=saved_action.created_at,
            updated_at=datetime.now(timezone.utc)
        )
        
        # 更新
        result = repository.update_service_action(updated_action)
        
        # 検証
        assert result.id == saved_action.id
        assert result.description == "Updated description"
        assert result.access_level == EAccessLevel.書き込み
        assert len(result.resource_types) == 2
        assert len(result.condition_keys) == 2

    def test_update_service_action_not_found(self, repository: ServiceActionPostgreSQLRepository):
        """存在しないService Actionの更新をテスト"""
        action = ServiceAction.new(
            service_prefix="nonexistent",
            action_name="Action",
            action_url="https://docs.aws.amazon.com/test.html",
            description="Test",
            access_level=EAccessLevel.読み込み,
        )
        
        with pytest.raises(ValueError, match="Service Action with id nonexistent:Action not found"):
            repository.update_service_action(action)

    def test_delete_service_actions_before(self, repository: ServiceActionPostgreSQLRepository):
        """指定日時より古いService Actionの削除をテスト"""
        now = datetime.now(timezone.utc)
        
        # 古いアクション
        old_action = ServiceAction.new(
            service_prefix="s3",
            action_name="OldAction",
            action_url="https://docs.aws.amazon.com/test.html",
            description="Old action",
            access_level=EAccessLevel.読み込み,
        )
        old_action.updated_at = datetime(2023, 1, 1, tzinfo=timezone.utc)
        
        # 新しいアクション
        new_action = ServiceAction.new(
            service_prefix="s3",
            action_name="NewAction",
            action_url="https://docs.aws.amazon.com/test.html",
            description="New action",
            access_level=EAccessLevel.読み込み,
        )
        
        # 保存
        repository.save_service_action(old_action)
        repository.save_service_action(new_action)
        
        # 2024年以前のアクションを削除
        deleted_count = repository.delete_service_actions_before(datetime(2024, 1, 1, tzinfo=timezone.utc))
        
        assert deleted_count == 1
        
        # 確認
        assert repository.get_service_action("s3:OldAction") is None
        assert repository.get_service_action("s3:NewAction") is not None

    def test_get_service_actions_with_criteria(self, repository: ServiceActionPostgreSQLRepository):
        """検索条件でのService Action取得をテスト"""
        # テストデータを作成
        actions = [
            ServiceAction.new(
                service_prefix="s3",
                action_name="GetObject",
                action_url="https://docs.aws.amazon.com/test.html",
                description="Get object from S3",
                access_level=EAccessLevel.読み込み,
            ),
            ServiceAction.new(
                service_prefix="s3",
                action_name="PutObject",
                action_url="https://docs.aws.amazon.com/test.html",
                description="Put object to S3",
                access_level=EAccessLevel.書き込み,
            ),
            ServiceAction.new(
                service_prefix="ec2",
                action_name="DescribeInstances",
                action_url="https://docs.aws.amazon.com/test.html",
                description="Describe EC2 instances",
                access_level=EAccessLevel.リスト,
            ),
        ]
        
        # 保存
        repository.save_service_actions(actions)
        
        # サービス名で検索
        criteria = VServiceActionSearchCriteria.new(
            service_name="s3",
            limit=10,
            offset=0
        )
        
        results = repository.get_service_actions(criteria)
        assert len(results) == 2
        assert all(action.service_prefix == "s3" for action in results)
        
        # アクセスレベルで検索
        criteria = VServiceActionSearchCriteria.new(
            access_level=EAccessLevel.読み込み,
            limit=10,
            offset=0
        )
        
        results = repository.get_service_actions(criteria)
        assert len(results) == 1
        assert results[0].access_level == EAccessLevel.読み込み

    def test_count_service_actions(self, repository: ServiceActionPostgreSQLRepository):
        """Service Actionの件数取得をテスト"""
        # テストデータを作成
        actions = [
            ServiceAction.new(
                service_prefix="s3",
                action_name="GetObject",
                action_url="https://docs.aws.amazon.com/test.html",
                description="Get object",
                access_level=EAccessLevel.読み込み,
            ),
            ServiceAction.new(
                service_prefix="s3",
                action_name="PutObject",
                action_url="https://docs.aws.amazon.com/test.html",
                description="Put object",
                access_level=EAccessLevel.書き込み,
            ),
        ]
        
        # 保存
        repository.save_service_actions(actions)
        
        # 全件数
        criteria = VServiceActionSearchCriteria.new(limit=10, offset=0)
        count = repository.count_service_actions(criteria)
        assert count == 2
        
        # 条件付き件数
        criteria = VServiceActionSearchCriteria.new(
            service_name="s3",
            limit=10,
            offset=0
        )
        count = repository.count_service_actions(criteria)
        assert count == 2

    def test_get_last_updated(self, repository: ServiceActionPostgreSQLRepository):
        """最終更新日時の取得をテスト"""
        # データが無い場合
        last_updated = repository.get_last_updated()
        assert last_updated is None
        
        # データを保存
        action = ServiceAction.new(
            service_prefix="s3",
            action_name="GetObject",
            action_url="https://docs.aws.amazon.com/test.html",
            description="Get object",
            access_level=EAccessLevel.読み込み,
        )
        saved_action = repository.save_service_action(action)
        
        # 最終更新日時を取得
        last_updated = repository.get_last_updated()
        assert last_updated is not None
        assert last_updated >= saved_action.updated_at
