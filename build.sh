#!/bin/bash
set -e

echo "Installing system dependencies..."
apt-get update
apt-get install -y postgresql-client

echo "Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Generating Prisma client..."
prisma generate

echo "Build complete!"
