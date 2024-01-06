from functools import lru_cache
import os
from pydantic import Field

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_DRIVER: str
    API_VERSION: str
    APP_NAME: str

    DATABASE_DIALECT: str
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_USERNAME: str
    DEBUG_MODE: bool

    class Config:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src_dir = os.path.dirname(current_dir)
        env_file = os.path.join(src_dir, '.env')
        env_file_encoding = "utf-8"


    @property
    def database_url(self) -> str:
        """Create a valid Postgres database url."""
        return f"postgresql+{self.DB_DRIVER}://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOSTNAME}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"



settings = Settings()
