from sqlmodel import SQLModel, Field, Column
from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import ARRAY, String, Text, CheckConstraint
from src.domain.service_action.entity import ServiceAction, EAccessLevel


class MServiceAction(SQLModel, table=True):
    """Service ActionのSQLModelエンティティ"""

    __tablename__ = "service_actions"

    id: str = Field(primary_key=True, max_length=255)
    service_prefix: str = Field(max_length=100, index=True)
    service_name: str = Field(max_length=255, index=True)
    action_name: str = Field(max_length=255, index=True)
    action_url: str = Field(sa_column=Column(Text))
    description: str = Field(sa_column=Column(Text))
    access_level: str = Field(max_length=50, index=True)
    resource_types: Optional[List[str]] = Field(
        default=None, sa_column=Column(ARRAY(String))
    )
    condition_keys: Optional[List[str]] = Field(
        default=None, sa_column=Column(ARRAY(String))
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), index=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), index=True
    )

    __table_args__ = (
        CheckConstraint(
            "access_level IN ('List', 'Read', 'Write', 'Permissions management', 'Tagging')",
            name="chk_access_level",
        ),
        CheckConstraint(
            "action_url LIKE 'https://docs.aws.amazon.com%'",
            name="chk_action_url_domain",
        ),
        CheckConstraint(
            "id ~ '^[a-zA-Z0-9_-]+:[a-zA-Z0-9_*-]+$'", name="chk_id_format"
        ),
    )

    @classmethod
    def from_entity(cls, service_action: ServiceAction) -> "MServiceAction":
        """ドメインエンティティからSQLModelエンティティを作成"""
        return cls(
            id=service_action.id,
            service_prefix=service_action.service_prefix,
            service_name=service_action.service_name,
            action_name=service_action.action_name,
            action_url=service_action.action_url,
            description=service_action.description,
            access_level=service_action.access_level.value,
            resource_types=(
                service_action.resource_types if service_action.resource_types else None
            ),
            condition_keys=(
                service_action.condition_keys if service_action.condition_keys else None
            ),
            created_at=service_action.created_at,
            updated_at=service_action.updated_at,
        )

    def to_entity(self) -> ServiceAction:
        """SQLModelエンティティからドメインエンティティを作成"""
        return ServiceAction.reconstruct(
            id=self.id,
            service_prefix=self.service_prefix,
            service_name=self.service_name,
            action_name=self.action_name,
            action_url=self.action_url,
            description=self.description,
            access_level=self.access_level,
            resource_types=self.resource_types or [],
            condition_keys=self.condition_keys or [],
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
