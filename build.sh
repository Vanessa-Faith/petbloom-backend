#!/bin/bash
set -e

echo "Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Generating Prisma client..."
prisma generate

echo "Build complete!"
