#!/bin/bash
set -e

echo "Running Prisma migrations..."
prisma db push --skip-generate

echo "Starting server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
