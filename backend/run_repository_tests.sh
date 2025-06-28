#!/bin/bash

# テスト用PostgreSQLコンテナの起動とテスト実行スクリプト

set -e

# venv環境をアクティベート
if [ -f "venv/bin/activate" ]; then
    echo "Activating Python virtual environment..."
    source venv/bin/activate
elif [ -f "../venv/bin/activate" ]; then
    echo "Activating Python virtual environment..."
    source ../venv/bin/activate
else
    echo "Warning: Python virtual environment not found. Using system Python."
fi

echo "Starting test PostgreSQL container..."
sudo docker-compose -f docker-compose.test.yml up -d test-postgres

# PostgreSQLが起動するまで待機
echo "Waiting for PostgreSQL to be ready..."
until sudo docker exec test-postgres-iamgate pg_isready -U test -d test_iamgate; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

echo "PostgreSQL container is ready! Checking external connectivity..."

# 外部からの接続も確認（Python側からの接続テスト）
echo "Testing database connection from host..."
max_attempts=30
attempt=1

while [ $attempt -le $max_attempts ]; do
  echo "Connection attempt $attempt/$max_attempts..."
  if python -c "
import psycopg2
try:
    conn = psycopg2.connect(
        host='localhost',
        port=5433,
        user='test',
        password='test',
        database='test_iamgate'
    )
    conn.close()
    print('Successfully connected to PostgreSQL!')
    exit(0)
except Exception as e:
    print(f'Connection failed: {e}')
    exit(1)
" 2>/dev/null; then
    echo "Database connection successful!"
    break
  else
    echo "Database connection failed, waiting..."
    sleep 2
    attempt=$((attempt + 1))
  fi
done

if [ $attempt -gt $max_attempts ]; then
  echo "Failed to connect to database after $max_attempts attempts"
  echo "Stopping test containers..."
  sudo docker-compose -f docker-compose.test.yml down
  exit 1
fi

# 必要なパッケージがインストールされているか確認
echo "Checking required packages..."
python -c "import pytest, psycopg2" 2>/dev/null || {
    echo "Installing required test packages..."
    pip install pytest pytest-asyncio psycopg2-binary
}

# テスト実行
echo "Running repository tests..."
python -m pytest tests/infrastructure/service_action/test_service_action_postgresql_repository.py -v

# テスト完了後にコンテナを停止
echo "Stopping test containers..."
sudo docker-compose -f docker-compose.test.yml down

echo "Test completed!"

# venv環境をdeactivate
if [ -n "$VIRTUAL_ENV" ]; then
    deactivate
fi
