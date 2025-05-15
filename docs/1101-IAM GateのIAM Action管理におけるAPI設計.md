# IAM GateのIAM Action管理におけるAPI設計

## 概要
IAM GateのIAM Action管理に必要なAPI設計を、ユースケース（1001）に基づき整理します。

---

## API一覧

### 1. IAM Actionの参照系

- **GET /iam-actions**
  - IAM Actionの一覧取得（サービス指定・検索・フィルタ・件数取得・最終更新日時取得を含む）
  - クエリパラメータ例:
    - `service`（サービス名で絞り込み）
    - `action_name`（部分一致・完全一致・正規表現検索）
    - `description`（説明文の部分一致検索）
    - `level`（アクションレベルでフィルタ）
    - `count_only`（件数のみ取得）
    - `updated_after`（最終更新日時でフィルタ）
    - `updated_before`（最終更新日時でフィルタ）
    - `limit`（取得件数制限）
    - `offset`（取得件数のオフセット）
    - `sort`（ソート条件）
    - `order`（昇順・降順）

---

### 2. IAM Actionの登録系

- **POST /iam-actions**
  - IAM Actionの新規登録
  - リクエストボディ例:
    - `service`, `service_prefix`, `action_name`, `description`, `detail_url`, `level`
    - (Optional) `resource_types`, `condition_keys`

---

### 3. IAM Actionの更新系

- **PUT /iam-actions/{action_id}**
  - IAM Actionの更新
  - リクエストボディ例:
    - 上記登録と同様

---

### 4. IAM Actionの削除系

- **DELETE /iam-actions**
  - 最終更新日時が特定日時より古いIAM Actionの一括削除
  - クエリパラメータ例:
    - `updated_before`（この日時より古いものを削除）

---

## 備考

- 認可・認証はアクターごとに制御（管理者・一般ユーザー・クローラー等）
- 検索・フィルタ・件数取得・最終更新日時取得はパラメータで柔軟に対応
- Optional項目（リソースタイプ・条件キー等）は拡張性を持たせる

---

この設計をもとにAPI仕様書やOpenAPI定義を作成できます。