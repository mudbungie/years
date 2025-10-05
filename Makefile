.PHONY: help install dev test test-watch lint format docker-build docker-run clean
.PHONY: init-db tf-init tf-plan tf-apply tf-destroy tf-output update-env

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Development setup
install: ## Install dependencies
	uv sync

dev: ## Run development server
	@set -a && . .env.dev && set +a && uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Testing
test: ## Run tests
	@YEARS_TESTING=true uv run pytest -v

test-watch: ## Run tests in watch mode
	@YEARS_TESTING=true uv run pytest-watch -v

# Code quality
lint: ## Run linters
	uv run ruff check .
	uv run black --check .

format: ## Format code
	uv run ruff --fix .
	uv run black .

# Docker
docker-build: ## Build Docker image
	docker build -t years .

docker-run: ## Run Docker container
	docker run -p 8000:8000 years

# Database
init-db: ## Initialize database schema
	@set -a && . .env.dev && set +a && uv run python scripts/init_db.py

# Terraform
tf-init: ## Initialize Terraform
	cd terraform && terraform init

tf-plan: ## Plan Terraform changes
	cd terraform && terraform plan

tf-apply: ## Apply Terraform changes
	cd terraform && terraform apply

tf-destroy: ## Destroy Terraform resources
	cd terraform && terraform destroy

tf-output: ## Show Terraform outputs
	cd terraform && terraform output

update-env: ## Update .env.dev with Terraform outputs
	@echo "Updating .env.dev with Terraform outputs..."
	@cd terraform && \
		sed -i 's|YEARS_DB_HOST=.*|YEARS_DB_HOST='$$(terraform output -raw db_host)'|' ../.env.dev && \
		sed -i 's|YEARS_DB_SERVICE=.*|YEARS_DB_SERVICE='$$(terraform output -raw db_service_name)'|' ../.env.dev
	@echo "Updated .env.dev - set YEARS_DB_PASSWORD manually"

# Cleanup
clean: ## Clean build artifacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
	find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	docker system prune -f