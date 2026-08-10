#!/bin/sh

echo "Waiting for PostgreSQL..."

until alembic current >/dev/null 2>&1
do
    echo "PostgreSQL is not ready yet..."
    sleep 2
done

echo "PostgreSQL is ready!"

echo "Running database migrations..."
alembic upgrade head

echo "Starting FastAPI..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}