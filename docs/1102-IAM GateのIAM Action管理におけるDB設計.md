# IAM GateのIAM Action管理におけるDB設計

## 概要

IAM GateのIAM Action管理に必要なDB設計を、ユースケース（1001）に基づき整理します。

---

## DB設計

### 1. IAM Actionテーブル

- **iam_actions**
  - IAM Actionの情報を格納するテーブル
  - カラム例:
    - `id`（主キー, `service_prefix:action_name`）
    - `service_name`（サービス名）
    - `service_prefix`（サービスプレフィックス）
    - `action_name`（アクション名）
    - `description`（アクションの説明文）
    - `detail_url`（アクションの詳細ページURL）
    - `level`（アクションレベル）
    - `created_at`（作成日時）
    - `updated_at`（最終更新日時）
    - `deleted_at`（削除日時、論理削除用）
    - `optional`（オプション情報, 備考や作成者、更新者、削除者など、現状検索で利用予定のないもの）

  - Index対象列一覧:
    - `service_name`（サービス名, pg_trgm拡張 + GIN Index）
    - `level`（アクションレベル）
    - `updated_at`（作成日時）
