#!/bin/bash

cd "$(dirname "$0")"
source venv/bin/activate

echo "Starting backend on port 8000..."
python -m uvicorn backend.api:app --port 8000 &

sleep 3

echo "Starting frontend on port 5000..."
python frontend/app.py
