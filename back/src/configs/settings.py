import os
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_DRIVER: str
    API_VERSION: str
    APP_NAME: str
    DB_DIALECT: str
    DB_HOSTNAME: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_USERNAME: str
    DEBUG_MODE: bool
    PYTHONDONTWRITEBYTECODE: str
    PYTHONUNBUFFERED: str
    JWT_EXPIRE: str
    JWT_ALGORITHM: str

    class Config:
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        env_file = os.path.join(BASE_DIR, ".env")
        env_file_encoding = "utf-8"

    @property
    def database_url(self) -> str:
        """Create a valid Postgres database url."""
        return f"postgresql+{self.DB_DRIVER}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOSTNAME}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
