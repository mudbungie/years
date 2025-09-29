from fastapi import FastAPI
from datetime import datetime, UTC

app = FastAPI(
    title="Years",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(UTC).isoformat()
    }
