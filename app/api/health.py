"""Health check endpoint."""
from datetime import datetime, UTC
from fastapi import APIRouter, status
from pydantic import BaseModel

from app.db.base import test_connection

router = APIRouter()


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    timestamp: str
    database: str


@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    tags=["Health"]
)
async def health_check():
    """
    Health check endpoint.
    
    Returns service status and database connectivity.
    """
    db_status = "healthy" if test_connection() else "unhealthy"
    
    return {
        "status": "healthy" if db_status == "healthy" else "degraded",
        "timestamp": datetime.now(UTC).isoformat(),
        "database": db_status
    }
