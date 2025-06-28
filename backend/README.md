# IAM Gate Backend

IAM Action管理システムのバックエンドAPI

## 開発環境のセットアップ

### 1. 仮想環境の作成と依存関係のインストール

```bash
# 推奨: Makefileを使用（自動でvenv環境を作成・管理）
make setup

# または手動で実行
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pytest pytest-asyncio psycopg2-binary
```

### 2. 開発時の注意事項

- **必ずvenv環境をアクティベートしてから作業してください**
- VSCodeの統合ターミナルでは自動でvenv環境がアクティベートされます
- コマンドライン作業時は: `source venv/bin/activate`

## テストの実行

### 基本テスト
```bash
make test
# または
source venv/bin/activate && python -m pytest tests/ -v
```

### リポジトリテスト（PostgreSQL付き）
```bash
make test-repo
# または
./run_repository_tests.sh
```

### すべてのテスト（Docker環境）
```bash
make docker-test
```

## Makeコマンド一覧

| コマンド | 説明 |
|----------|------|
| `make help` | 利用可能なコマンドを表示 |
| `make venv` | Python仮想環境を作成 |
| `make install` | 依存関係をインストール |
| `make setup` | 開発環境の初期セットアップ |
| `make test` | 基本テストを実行 |
| `make test-repo` | リポジトリテスト（PostgreSQL付き）を実行 |
| `make clean` | コンテナとキャッシュをクリーンアップ |
| `make docker-test` | Docker環境でテストを実行 |

## プロジェクト構造

```
backend/
├── src/
│   ├── domain/           # ドメイン層
│   │   └── service_action/
│   ├── infrastructure/   # インフラストラクチャ層
│   │   └── service_action/
│   └── usecase/         # ユースケース層
├── tests/               # テストコード
├── requirements.txt     # Python依存関係
├── Makefile            # 開発タスク定義
└── run_repository_tests.sh  # リポジトリテスト実行スクリプト
```

## 重要: 仮想環境について

このプロジェクトでは **Python仮想環境 (venv)** を使用しています。

### 仮想環境を忘れないための対策

1. **VSCode設定**: `.vscode/settings.json`で自動的にvenv環境を使用
2. **ターミナル初期化**: `.vscode/terminal_init.sh`で自動アクティベート
3. **Makefile**: すべてのタスクでvenv環境を自動使用
4. **スクリプト**: `run_repository_tests.sh`でvenv環境を自動検出・使用

### トラブルシューティング

#### venv環境が見つからない場合
```bash
make venv      # 仮想環境を作成
make install   # 依存関係をインストール
```

#### PostgreSQLコンテナの問題
```bash
make clean     # コンテナとキャッシュをクリーンアップ
make test-repo # 再度テストを実行
```

#### 権限の問題
```bash
sudo usermod -aG docker $USER  # Dockerグループに追加
newgrp docker                   # グループを再読み込み
```
