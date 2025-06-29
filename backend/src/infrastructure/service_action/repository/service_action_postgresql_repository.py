from datetime import datetime
from typing import Optional
from sqlmodel import Session, select, func, text
from sqlalchemy import Engine, or_, and_

from src.domain.service_action.repository import IServiceActionRepository
from src.domain.service_action.entity import ServiceAction
from src.domain.service_action.value_object import (
    VServiceActionSearchCriteria,
    EActionNameMatch,
    EOrder,
)
from ..model import MServiceAction


class ServiceActionPostgreSQLRepository(IServiceActionRepository):
    """Service ActionのPostgreSQLリポジトリ実装"""

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def get_service_action(self, id: str) -> Optional[ServiceAction]:
        """指定されたIDのService Actionを取得"""
        with Session(self.engine) as session:
            statement = select(MServiceAction).where(MServiceAction.id == id)
            result = session.exec(statement)
            db_action = result.first()

            if db_action is None:
                return None

            return db_action.to_entity()

    def get_service_actions(
        self, criteria: VServiceActionSearchCriteria
    ) -> list[ServiceAction]:
        """検索条件に基づいてService Actionの一覧を取得"""
        if criteria.count_only:
            return []

        with Session(self.engine) as session:
            statement = self._build_search_query(criteria)
            statement = self._apply_pagination_and_sort(statement, criteria)

            result = session.exec(statement)
            db_actions = result.all()

            return [db_action.to_entity() for db_action in db_actions]

    def count_service_actions(self, criteria: VServiceActionSearchCriteria) -> int:
        """検索条件に基づいてService Actionの件数を取得"""
        with Session(self.engine) as session:
            base_query = self._build_search_query(criteria, count_only=True)
            count_statement = select(func.count()).select_from(base_query.subquery())

            result = session.exec(count_statement)
            return result.one()

    def get_last_updated(self) -> Optional[datetime]:
        """最後に更新されたService Actionの更新日時を取得"""
        with Session(self.engine) as session:
            statement = select(func.max(MServiceAction.updated_at))
            result = session.exec(statement)
            return result.one()

    def save_service_action(self, action: ServiceAction) -> ServiceAction:
        """Service Actionを保存（upsert）"""
        with Session(self.engine) as session:
            db_action = MServiceAction.from_entity(action)
            session.merge(db_action)  # upsert
            session.commit()
            session.refresh(db_action)
            return db_action.to_entity()

    def save_service_actions(self, actions: list[ServiceAction]) -> list[ServiceAction]:
        """複数のService Actionを一括保存"""
        if not actions:
            return []

        with Session(self.engine) as session:
            db_actions = [MServiceAction.from_entity(action) for action in actions]

            for db_action in db_actions:
                session.merge(db_action)  # upsert

            session.commit()

            # refresh all objects
            for db_action in db_actions:
                session.refresh(db_action)

            return [db_action.to_entity() for db_action in db_actions]

    def update_service_action(self, action: ServiceAction) -> ServiceAction:
        """既存のService Actionを更新"""
        with Session(self.engine) as session:
            statement = select(MServiceAction).where(MServiceAction.id == action.id)
            result = session.exec(statement)
            db_action = result.first()

            if db_action is None:
                raise ValueError(f"Service Action with id {action.id} not found")

            # 更新
            db_action.service_prefix = action.service_prefix
            db_action.action_name = action.action_name
            db_action.action_url = action.action_url
            db_action.description = action.description
            db_action.access_level = action.access_level.value
            db_action.resource_types = (
                action.resource_types if action.resource_types else None
            )
            db_action.condition_keys = (
                action.condition_keys if action.condition_keys else None
            )
            db_action.updated_at = action.updated_at

            session.add(db_action)
            session.commit()
            session.refresh(db_action)

            return db_action.to_entity()

    def delete_service_actions_before(self, updated_before: datetime) -> int:
        """指定日時より古いService Actionを削除"""
        with Session(self.engine) as session:
            statement = select(MServiceAction).where(
                MServiceAction.updated_at < updated_before
            )
            result = session.exec(statement)
            actions_to_delete = result.all()

            count = len(actions_to_delete)

            for action in actions_to_delete:
                session.delete(action)

            session.commit()
            return count

    def _build_search_query(
        self, criteria: VServiceActionSearchCriteria, count_only: bool = False
    ):
        """検索条件からクエリを構築"""
        if count_only:
            statement = select(MServiceAction.id)
        else:
            statement = select(MServiceAction)

        # 検索条件を適用
        conditions = []

        # service_prefixでの検索（IAMアクションプレフィックス: s3, ec2など）
        if criteria.service_prefix:
            from sqlalchemy import func

            conditions.append(
                func.lower(MServiceAction.service_prefix).like(
                    f"%{criteria.service_prefix.lower()}%"
                )
            )

        # service_nameでの検索（公式サービス名: Amazon S3, Amazon EC2など）
        if criteria.service_name:
            from sqlalchemy import func

            conditions.append(
                func.lower(MServiceAction.service_name).like(
                    f"%{criteria.service_name.lower()}%"
                )
            )

        if criteria.action_name:
            if criteria.action_name_match == EActionNameMatch.exact:
                conditions.append(MServiceAction.action_name == criteria.action_name)
            elif criteria.action_name_match == EActionNameMatch.partial:
                from sqlalchemy import func

                conditions.append(
                    func.lower(MServiceAction.action_name).like(
                        f"%{criteria.action_name.lower()}%"
                    )
                )
            elif criteria.action_name_match == EActionNameMatch.regex:
                # 正規表現の長さをチェック（安全のため）
                if not criteria.validate_regex_pattern():
                    raise ValueError(
                        "Regular expression pattern is too long (max 500 characters)"
                    )
                # PostgreSQLの正規表現演算子を使用
                conditions.append(
                    MServiceAction.action_name.op("~")(criteria.action_name)
                )

        if criteria.description:
            from sqlalchemy import func

            conditions.append(
                func.lower(MServiceAction.description).like(
                    f"%{criteria.description.lower()}%"
                )
            )

        if criteria.access_level:
            conditions.append(
                MServiceAction.access_level == criteria.access_level.value
            )

        if criteria.updated_after:
            conditions.append(MServiceAction.updated_at >= criteria.updated_after)

        if criteria.updated_before:
            conditions.append(MServiceAction.updated_at <= criteria.updated_before)

        if conditions:
            statement = statement.where(and_(*conditions))

        return statement

    def _apply_pagination_and_sort(
        self, statement, criteria: VServiceActionSearchCriteria
    ):
        """ページネーションとソートを適用"""
        # ソート
        sort_column = getattr(MServiceAction, criteria.sort, MServiceAction.id)
        if criteria.order == EOrder.desc:
            statement = statement.order_by(sort_column.desc())
        else:
            statement = statement.order_by(sort_column.asc())

        # ページネーション
        statement = statement.offset(criteria.offset).limit(criteria.limit)

        return statement
