import os

from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool
    DB_DRIVER: str
    API_VERSION: str
    APP_NAME: str
    DB_DIALECT: str
    DB_HOSTNAME: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_USERNAME: str
    PYTHONDONTWRITEBYTECODE: str
    PYTHONUNBUFFERED: str
    JWT_ACCESS_LIFETIME: int
    JWT_REFRESH_LIFETIME: str
    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str

    class Config:
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        env_file = os.path.join(BASE_DIR, ".env")
        print(env_file)
        env_file_encoding = "utf-8"

    @property
    def database_url(self) -> str:
        """Create a valid Postgres database url."""
        return f"postgresql+{self.DB_DRIVER}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOSTNAME}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
