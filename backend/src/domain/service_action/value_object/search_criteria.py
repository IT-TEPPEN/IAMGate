from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from typing import Optional
from ..entity import EAccessLevel


class EActionNameMatch(str, Enum):
    """検索方式の列挙型"""

    partial = "partial"
    exact = "exact"
    regex = "regex"


class EOrder(str, Enum):
    """ソート順の列挙型"""

    asc = "asc"
    desc = "desc"


class VServiceActionSearchCriteria(BaseModel):
    """Service Action検索条件の値オブジェクト"""

    # 検索条件
    service_name: Optional[str] = None
    action_name: Optional[str] = None
    action_name_match: EActionNameMatch = EActionNameMatch.partial
    description: Optional[str] = None
    access_level: Optional[EAccessLevel] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None

    # ページネーション
    limit: int = Field(default=100, ge=1, le=1000)
    offset: int = Field(default=0, ge=0)

    # ソート
    sort: str = Field(default="id")
    order: EOrder = EOrder.asc

    # 件数のみ取得フラグ
    count_only: bool = False

    def validate_regex_pattern(self) -> bool:
        """正規表現パターンのバリデーション"""
        if (
            self.action_name_match == EActionNameMatch.regex
            and self.action_name
            and len(self.action_name) > 500
        ):
            return False
        return True

    @classmethod
    def new(
        cls,
        service_name: Optional[str] = None,
        action_name: Optional[str] = None,
        action_name_match: EActionNameMatch = EActionNameMatch.partial,
        description: Optional[str] = None,
        access_level: Optional[EAccessLevel] = None,
        updated_after: Optional[datetime] = None,
        updated_before: Optional[datetime] = None,
        limit: int = 100,
        offset: int = 0,
        sort: str = "id",
        order: EOrder = EOrder.asc,
        count_only: bool = False,
    ) -> "VServiceActionSearchCriteria":
        """新しい検索条件を作成"""
        return cls(
            service_name=service_name,
            action_name=action_name,
            action_name_match=action_name_match,
            description=description,
            access_level=access_level,
            updated_after=updated_after,
            updated_before=updated_before,
            limit=limit,
            offset=offset,
            sort=sort,
            order=order,
            count_only=count_only,
        )
