# Podcast Audio Processing API

Basic audio analysis and segmentation for podcast files using deterministic algorithms.

## Setup

```bash
# Install dependencies
uv sync

# Run development server
make dev

# Run tests
make test

# Check health endpoint
curl http://localhost:8000/health
```

## Project Structure

```
app/
├── api/          # API endpoints
├── core/         # Configuration and settings
├── db/           # Database models and connection
├── models/       # Pydantic models
├── services/     # Business logic
└── main.py       # FastAPI application

tests/
├── api/          # API endpoint tests
├── unit/         # Unit tests
└── integration/  # Integration tests
```

## Dependencies

- **FastAPI**: Web framework
- **LibROSA**: Audio analysis
- **PyDub**: Audio manipulation
- **OracleDB**: Database connectivity
- **SQLAlchemy**: Object Relational Mapping (ORM)

## Docker

```bash
# Build image
make docker-build

# Run container
make docker-run
```

## Development

```bash
# Format code
make format

# Run linting
make lint

# Clean cache
make clean
```
