from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from ..entity import ServiceAction
from ..value_object import VServiceActionSearchCriteria


class IServiceActionRepository(ABC):
    """Service Actionリポジトリのインターフェース"""

    # 参照系
    @abstractmethod
    def get_service_action(self, id: str) -> Optional[ServiceAction]:
        """
        指定されたIDのService Actionを取得

        :param id: Service ActionのID (service_prefix:action_name形式)
        :return: Service Action、存在しない場合はNone
        """
        pass

    @abstractmethod
    def get_service_actions(
        self, criteria: VServiceActionSearchCriteria
    ) -> list[ServiceAction]:
        """
        検索条件に基づいてService Actionの一覧を取得

        :param criteria: 検索条件
        :return: Service Actionのリスト
        """
        pass

    @abstractmethod
    def count_service_actions(self, criteria: VServiceActionSearchCriteria) -> int:
        """
        検索条件に基づいてService Actionの件数を取得

        :param criteria: 検索条件
        :return: 件数
        """
        pass

    @abstractmethod
    def get_last_updated(self) -> Optional[datetime]:
        """
        最後に更新されたService Actionの更新日時を取得

        :return: 最終更新日時、データが存在しない場合はNone
        """
        pass

    # 更新系
    @abstractmethod
    def save_service_action(self, action: ServiceAction) -> ServiceAction:
        """
        Service Actionを保存（新規作成またはupsert）

        :param action: 保存するService Action
        :return: 保存されたService Action
        """
        pass

    @abstractmethod
    def save_service_actions(self, actions: list[ServiceAction]) -> list[ServiceAction]:
        """
        複数のService Actionを一括保存

        :param actions: 保存するService Actionのリスト
        :return: 保存されたService Actionのリスト
        """
        pass

    @abstractmethod
    def update_service_action(self, action: ServiceAction) -> ServiceAction:
        """
        既存のService Actionを更新

        :param action: 更新するService Action
        :return: 更新されたService Action
        :raises: アクションが存在しない場合は例外
        """
        pass

    @abstractmethod
    def delete_service_actions_before(self, updated_before: datetime) -> int:
        """
        指定日時より古いService Actionを削除

        :param updated_before: この日時より古いアクションを削除
        :return: 削除された件数
        """
        pass
