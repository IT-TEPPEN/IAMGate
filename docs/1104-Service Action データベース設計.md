# Service Action データベース設計

## 概要
Service ActionのPostgreSQLテーブル設計を定義します。

---

## テーブル設計

### service_actions テーブル

```sql
CREATE TABLE service_actions (
    id VARCHAR(255) PRIMARY KEY,  -- service_prefix:action_name 形式
    service_prefix VARCHAR(100) NOT NULL,
    action_name VARCHAR(255) NOT NULL,
    action_url TEXT NOT NULL,
    description TEXT NOT NULL,
    access_level VARCHAR(50) NOT NULL,
    resource_types TEXT[],  -- PostgreSQL配列型
    condition_keys TEXT[],  -- PostgreSQL配列型
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    
    -- 制約
    CONSTRAINT chk_access_level CHECK (
        access_level IN ('List', 'Read', 'Write', 'Permissions management', 'Tagging')
    ),
    CONSTRAINT chk_action_url_domain CHECK (
        action_url LIKE 'https://docs.aws.amazon.com%'
    ),
    CONSTRAINT chk_id_format CHECK (
        id ~ '^[a-zA-Z0-9_-]+:[a-zA-Z0-9_*-]+$'
    )
);
```

### インデックス設計

```sql
-- プライマリキー（自動作成）
-- PRIMARY KEY (id)

-- 検索性能向上のためのインデックス
CREATE INDEX idx_service_actions_service_prefix ON service_actions (service_prefix);
CREATE INDEX idx_service_actions_action_name ON service_actions (action_name);
CREATE INDEX idx_service_actions_access_level ON service_actions (access_level);
CREATE INDEX idx_service_actions_updated_at ON service_actions (updated_at);

-- 部分一致検索用のGINインデックス（PostgreSQL拡張）
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX idx_service_actions_action_name_trgm ON service_actions 
    USING gin (action_name gin_trgm_ops);
CREATE INDEX idx_service_actions_description_trgm ON service_actions 
    USING gin (description gin_trgm_ops);

-- 複合インデックス
CREATE INDEX idx_service_actions_service_prefix_action_name ON service_actions 
    (service_prefix, action_name);
```

---

## SQLModelエンティティ設計

### MServiceAction（データベースモデル）

```python
from sqlmodel import SQLModel, Field, Column
from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import ARRAY, String, Text, CheckConstraint
import uuid


class MServiceAction(SQLModel, table=True):
    """Service ActionのSQLModelエンティティ"""
    
    __tablename__ = "service_actions"
    
    id: str = Field(primary_key=True, max_length=255)
    service_name: str = Field(max_length=255, index=True)
    service_prefix: str = Field(max_length=100, index=True) 
    action_name: str = Field(max_length=255, index=True)
    action_url: str = Field(sa_column=Column(Text))
    description: str = Field(sa_column=Column(Text))
    access_level: str = Field(max_length=50, index=True)
    resource_types: Optional[List[str]] = Field(
        default=None, 
        sa_column=Column(ARRAY(String))
    )
    condition_keys: Optional[List[str]] = Field(
        default=None,
        sa_column=Column(ARRAY(String))
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        index=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        index=True
    )
    
    __table_args__ = (
        CheckConstraint(
            "access_level IN ('List', 'Read', 'Write', 'Permissions management', 'Tagging')",
            name="chk_access_level"
        ),
        CheckConstraint(
            "action_url LIKE 'https://docs.aws.amazon.com%'",
            name="chk_action_url_domain"
        ),
        CheckConstraint(
            "id ~ '^[a-zA-Z0-9_-]+:[a-zA-Z0-9_*-]+$'",
            name="chk_id_format"
        ),
    )
```

---

## 設計上の考慮事項

### 1. パフォーマンス
- **GINインデックス**: 部分一致検索の高速化
- **複合インデックス**: よく使われる検索条件の組み合わせ
- **配列型**: PostgreSQL固有の機能を活用

### 2. データ整合性
- **CHECK制約**: アクセスレベルとURL形式の検証
- **正規表現制約**: IDフォーマットの検証

### 3. 拡張性
- **配列フィールド**: resource_types, condition_keysの柔軟な格納
- **テキスト型**: 長い説明文やURLに対応

### 4. 検索性能
- **トライグラム**: 部分一致検索の高速化
- **個別インデックス**: 各検索条件に対応
