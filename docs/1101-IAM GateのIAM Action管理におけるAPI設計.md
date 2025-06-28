# IAM GateのIAM Action管理におけるAPI設計

## 概要
IAM GateのIAM Action管理に必要なAPI設計を、ユースケース（1001）に基づき整理します。

---

## API一覧

### バージョニング
- APIのバージョンはURLパスで管理（例: `/v1/iam-actions`）
- 同一バージョン内では後方互換性を保持
- 異なるバージョン間では後方互換性は必須ではない

### 1. IAM Actionの参照系

- **GET /v1/iam-actions**
  - IAM Actionの一覧取得（サービス指定・検索・フィルタ・件数取得・最終更新日時取得を含む）
  - クエリパラメータ:
    - `service`（サービス名で絞り込み）
    - `action_name`（アクション名検索）
      - `action_name_match`（検索方式: `partial`, `exact`, `regex`、デフォルト: `partial`）
    - `description`（説明文の部分一致検索）
    - `access_level`（アクセスレベルでフィルタ: `List`, `Read`, `Write`, `Permissions management`, `Tagging`）
    - `count_only`（件数のみ取得: `true`/`false`）
    - `updated_after`（最終更新日時でフィルタ: ISO8601形式）
    - `updated_before`（最終更新日時でフィルタ: ISO8601形式）
    - `limit`（取得件数制限: 1-1000、デフォルト: 100）
    - `offset`（取得件数のオフセット: 0以上、デフォルト: 0）
    - `sort`（ソート項目: `id`, `service_name`, `action_name`, `access_level`, `updated_at`）
    - `order`（昇順・降順: `asc`/`desc`、デフォルト: `asc`）
  
  - **検索機能の制限事項:**
    - 正規表現検索は文字数制限あり（最大500文字、ReDoS攻撃対策）
    - 複数検索条件はAND条件で組み合わせ
    - OR条件が必要な場合は複数回APIを呼び出し

---

### 2. IAM Actionの登録系

- **POST /v1/iam-actions**
  - IAM Actionの新規登録
  - リクエストボディ:
    - `service_name`（必須: サービス名）
    - `service_prefix`（必須: サービスプレフィックス）
    - `action_name`（必須: アクション名）
    - `description`（必須: アクション説明文）
    - `action_url`（必須: アクション詳細ページURL）
    - `access_level`（必須: アクセスレベル）
    - `resource_types`（任意: リソースタイプ配列）
    - `condition_keys`（任意: 条件キー配列）

---

### 3. IAM Actionの更新系

- **PUT /v1/iam-actions/{action_id}**
  - IAM Actionの更新（action_idは`service_prefix:action_name`形式）
  - リクエストボディ: 上記登録と同様

---

### 4. IAM Actionの削除系

- **DELETE /v1/iam-actions**
  - 最終更新日時が特定日時より古いIAM Actionの一括削除
  - 古いアクションの自動削除用途のため、事前確認・dry-run機能なし
  - クエリパラメータ:
    - `updated_before`（必須: この日時より古いものを削除、ISO8601形式）

---

## データモデル

### IAM Action
```json
{
  "id": "s3:GetObject",
  "service_name": "Amazon S3",
  "service_prefix": "s3",
  "action_name": "GetObject",
  "description": "オブジェクトを取得する権限",
  "action_url": "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-GetObject",
  "access_level": "Read",
  "resource_types": ["object"],
  "condition_keys": ["s3:ExistingObjectTag/*"],
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

### アクセスレベル
- `List`: リスト権限
- `Read`: 読み込み権限  
- `Write`: 書き込み権限
- `Permissions management`: 権限管理
- `Tagging`: タグ付け

---

## レスポンス形式

### 成功レスポンス

#### GET /v1/iam-actions（一覧取得）
```json
{
  "data": [
    // IAM Actionオブジェクトの配列
  ],
  "pagination": {
    "total_count": 1500,
    "current_page": 1,
    "per_page": 100,
    "total_pages": 15,
    "has_next": true,
    "has_prev": false
  },
  "meta": {
    "last_updated": "2024-01-01T12:00:00Z"
  }
}
```

#### GET /v1/iam-actions（件数のみ: count_only=true）
```json
{
  "total_count": 1500,
  "meta": {
    "last_updated": "2024-01-01T12:00:00Z"
  }
}
```

#### POST/PUT /v1/iam-actions
```json
{
  "data": {
    // 作成/更新されたIAM Actionオブジェクト
  }
}
```

#### DELETE /v1/iam-actions
```json
{
  "deleted_count": 25,
  "message": "2024-01-01T00:00:00Z より古い IAM Action を削除しました"
}
```

### エラーレスポンス
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "リクエストの形式が正しくありません",
    "details": [
      {
        "field": "access_level",
        "message": "無効なアクセスレベルです"
      }
    ]
  }
}
```

---

## 認証・認可

### アクター別アクセス権限
| エンドポイント           | IAM Gate管理者 | 一般ユーザー | 公式ドキュメントクローラー |
| :----------------------- | :------------: | :----------: | :------------------------: |
| GET /v1/iam-actions      |       ✓        |      ✓       |             ×              |
| POST /v1/iam-actions     |       ×        |      ×       |             ✓              |
| PUT /v1/iam-actions/{id} |       ×        |      ×       |             ✓              |
| DELETE /v1/iam-actions   |       ✓        |      ×       |             ×              |

### 認証方式
- **管理者・一般ユーザー**: JWT認証（有効期限1日、別の認証アプリで管理）
- **クローラー**: APIキー認証（別の認証アプリで管理）

---

## エラーコード

| HTTPステータス |     エラーコード      | 説明                                                  |
| :------------- | :-------------------: | :---------------------------------------------------- |
| 400            |   VALIDATION_ERROR    | リクエストの形式・値が無効                            |
| 401            |     UNAUTHORIZED      | 認証が必要または無効                                  |
| 403            |       FORBIDDEN       | アクセス権限なし                                      |
| 404            |       NOT_FOUND       | 指定されたリソースが存在しない                        |
| 409            |       CONFLICT        | リソースの競合（既存IDでの登録等）                    |
| 422            | UNPROCESSABLE_ENTITY  | 正規表現が500文字を超過、またはURLがAWSドメイン以外等 |
| 429            |   TOO_MANY_REQUESTS   | レート制限超過                                        |
| 500            | INTERNAL_SERVER_ERROR | サーバー内部エラー                                    |

---

## バリデーション・制限事項

### 正規表現検索
- 文字数制限: 最大500文字
- ReDoS攻撃対策のため、実行時間監視あり

### URL検証
- `action_url`は`docs.aws.amazon.com`ドメインのみ許可
- HTTPS必須

### データ処理
- 大量データ処理はCSVファイル等のバッチ処理で対応
- API経由の件数上限は設定しない（パフォーマンス要件は未定義）

---

## 備考

- 認証はJWT（1日有効）・APIキー共に別の認証アプリで管理
- 検索・フィルタ・件数取得・最終更新日時取得はパラメータで柔軟に対応
- 大量データ処理はCSVファイル等のバッチ処理で対応
- Optional項目（リソースタイプ・条件キー等）は拡張性を持たせる
