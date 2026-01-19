#!/bin/bash
set -e

echo "Starting PetBloom Backend..."

# Set default port if not provided
export PORT=${PORT:-8000}
echo "Using PORT: $PORT"

# Run database migrations if DATABASE_URL is set
if [ -n "$DATABASE_URL" ]; then
    echo "Running database migrations..."
    prisma db push --skip-generate || echo "Migration warning (non-fatal)"
else
    echo "WARNING: DATABASE_URL not set, skipping migrations"
fi

# Start the application
echo "Starting uvicorn on port $PORT..."
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
