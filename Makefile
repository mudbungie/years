.PHONY: install dev test lint format docker-build docker-run clean

# Development setup
install:
	uv sync

dev:
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Testing
test:
	uv run pytest

test-watch:
	uv run pytest --watch

# Code quality
lint:
	uv run ruff check .
	uv run black --check .

format:
	uv run ruff --fix .
	uv run black .

# Docker
docker-build:
	docker build -t audio-annotation-service .

docker-run:
	docker run -p 8000:8000 audio-annotation-service

# Cleanup
clean:
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	docker system prune -f
