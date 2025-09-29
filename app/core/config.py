import os
from typing import Optional

class Settings:
    # Database
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_HOST: str = os.getenv("DB_HOST", "")
    DB_PORT: int = int(os.getenv("DB_PORT", "1521"))
    DB_SERVICE: str = os.getenv("DB_SERVICE", "")
    
    # OCI Object Storage
    OCI_NAMESPACE: str = os.getenv("OCI_NAMESPACE", "")
    OCI_BUCKET_NAME: str = os.getenv("OCI_BUCKET_NAME", "podcast-audio")
    OCI_REGION: str = os.getenv("OCI_REGION", "")
    
    # File processing
    MAX_FILE_SIZE: int = int(os.getenv("MAX_FILE_SIZE", "524288000"))  # 500MB
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key")
    ALGORITHM: str = "HS256"
    
    # Rate limiting
    UPLOAD_RATE_LIMIT: int = int(os.getenv("UPLOAD_RATE_LIMIT", "10"))
    STATUS_RATE_LIMIT: int = int(os.getenv("STATUS_RATE_LIMIT", "100"))

settings = Settings()
