# app/config.py
from pydantic_settings import BaseSettings
from pathlib import Path
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Environment variables can be set directly or via a .env file.
    """
    app_name: str = "MobiCash Churn API"
    app_version: str = "1.0.0"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.

    Using lru_cache ensures settings are only loaded once.
    """
    return Settings()