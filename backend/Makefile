# Makefile for IAM Gate Backend Development

.PHONY: help venv install test test-repo clean docker-test

# デフォルトターゲット
help:
	@echo "Available commands:"
	@echo "  make venv        - Create Python virtual environment"
	@echo "  make install     - Install dependencies in venv"
	@echo "  make test        - Run all tests"
	@echo "  make test-repo   - Run repository tests with PostgreSQL"
	@echo "  make clean       - Clean up containers and cache"
	@echo "  make docker-test - Run tests in Docker environment"

# Python仮想環境の作成
venv:
	@if [ ! -d "venv" ]; then \
		echo "Creating Python virtual environment..."; \
		python3 -m venv venv; \
		echo "Virtual environment created. Activate with: source venv/bin/activate"; \
	else \
		echo "Virtual environment already exists."; \
	fi

# 依存関係のインストール
install: venv
	@if [ -f "venv/bin/activate" ]; then \
		echo "Installing dependencies in virtual environment..."; \
		. venv/bin/activate && pip install --upgrade pip; \
		. venv/bin/activate && pip install -r requirements.txt; \
		. venv/bin/activate && pip install pytest pytest-asyncio psycopg2-binary; \
		echo "Dependencies installed successfully."; \
	else \
		echo "Error: Virtual environment not found. Run 'make venv' first."; \
		exit 1; \
	fi

# 基本テストの実行
test:
	@if [ -f "venv/bin/activate" ]; then \
		echo "Running tests in virtual environment..."; \
		. venv/bin/activate && python -m pytest tests/ -v; \
	else \
		echo "Error: Virtual environment not found. Run 'make install' first."; \
		exit 1; \
	fi

# リポジトリテストの実行（PostgreSQL付き）
test-repo:
	@echo "Running repository tests with PostgreSQL..."
	@chmod +x run_repository_tests.sh
	@./run_repository_tests.sh

# クリーンアップ
clean:
	@echo "Cleaning up..."
	@sudo docker-compose -f docker-compose.test.yml down -v || true
	@sudo docker system prune -f || true
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "Cleanup completed."

# Docker環境でのテスト実行
docker-test: clean test-repo

# 開発環境のセットアップ
setup: venv install
	@echo "Development environment setup completed!"
	@echo "To activate the virtual environment, run: source venv/bin/activate"
