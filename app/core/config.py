"""Configuration management for Years API."""
import os
import sys


class Settings:
    """Application configuration."""
    
    # OCI Configuration
    TENANCY_OCID: str = os.getenv("YEARS_TENANCY_OCID", "")
    COMPARTMENT_OCID: str = os.getenv("YEARS_COMPARTMENT_OCID", "")
    REGION: str = os.getenv("YEARS_REGION", "us-sanjose-1")
    
    # Database configuration
    DB_HOST: str = os.getenv("YEARS_DB_HOST", "")
    DB_SERVICE: str = os.getenv("YEARS_DB_SERVICE", "")
    DB_USERNAME: str = os.getenv("YEARS_DB_USERNAME", "ADMIN")
    DB_PASSWORD: str = os.getenv("YEARS_DB_PASSWORD", "")
    DB_PORT: int = int(os.getenv("YEARS_DB_PORT", "1521"))
    
    # Object Storage
    OBJECT_STORAGE_NAMESPACE: str = os.getenv("YEARS_OBJECT_STORAGE_NAMESPACE", "")
    OBJECT_STORAGE_BUCKET: str = os.getenv("YEARS_OBJECT_STORAGE_BUCKET", "")
    
    # Queue Service
    QUEUE_OCID: str = os.getenv("YEARS_QUEUE_OCID", "")
    
    # API Configuration
    JWT_SECRET: str = os.getenv("YEARS_JWT_SECRET", "")
    API_BASE_URL: str = os.getenv("YEARS_API_BASE_URL", "http://localhost:8000")
    MAX_FILE_SIZE: int = int(os.getenv("YEARS_MAX_FILE_SIZE_MB", "500")) * 1024 * 1024
    
    # Development Settings
    ENV: str = os.getenv("YEARS_ENV", "development")
    DEBUG: bool = os.getenv("YEARS_DEBUG", "false").lower() == "true"
    TESTING: bool = os.getenv("YEARS_TESTING", "false").lower() == "true"
    
    # Rate limits
    UPLOAD_RATE_LIMIT: int = int(os.getenv("YEARS_UPLOAD_RATE_LIMIT", "10"))
    STATUS_RATE_LIMIT: int = int(os.getenv("YEARS_STATUS_RATE_LIMIT", "100"))
    
    def validate(self):
        """Validate required configuration."""
        if self.TESTING:
            return
            
        required = {
            "YEARS_TENANCY_OCID": self.TENANCY_OCID,
            "YEARS_COMPARTMENT_OCID": self.COMPARTMENT_OCID,
            "YEARS_DB_HOST": self.DB_HOST,
            "YEARS_DB_SERVICE": self.DB_SERVICE,
            "YEARS_DB_PASSWORD": self.DB_PASSWORD,
            "YEARS_JWT_SECRET": self.JWT_SECRET,
        }
        
        missing = [key for key, value in required.items() if not value]
        
        if missing:
            print(f"ERROR: Missing required environment variables: {', '.join(missing)}")
            sys.exit(1)


settings = Settings()
settings.validate()