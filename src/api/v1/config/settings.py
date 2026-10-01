from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, field_validator
from typing import List, Optional

class Settings(BaseSettings):
    APP_NAME: str = "Banco Digital API"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = False

    # Configuración CORS
    CORS_ORIGINS: List[str] = ["http://localhost", "http://localhost:3000"]

    # Configuración JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Configuración de base de datos
    DATABASE_URL: PostgresDsn
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10

    # Configuración de seguridad
    PASSWORD_HASH_ALGORITHM: str = "bcrypt"
    IDEMPOTENCY_KEY_EXPIRE_HOURS: int = 24

    class Config:
        env_file = ".env"
        case_sensitive = True

    @field_validator('DATABASE_URL', mode='before')
    def validate_database_url(cls, v):
        if not v:
            raise ValueError("DATABASE_URL no puede estar vacío")
        return v

    @field_validator('JWT_SECRET_KEY', mode='before')
    def validate_jwt_secret(cls, v):
        if not v or len(v) < 32:
            raise ValueError("JWT_SECRET_KEY debe tener al menos 32 caracteres")
        return v

settings = Settings()
"