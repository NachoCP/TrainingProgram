import os
from functools import lru_cache

from pydantic_settings import BaseSettings


@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    DATABASE_DIALECT: str
    DATABASE_HOSTNAME: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_USERNAME: str

    @property
    def database_url(self) -> str:
        return (f"{self.DATABASE_DIALECT}://{self.DATABASE_USERNAME}:"
                f"{self.DATABASE_PASSWORD}@{self.DATABASE_HOSTNAME}:"
                f"{self.DATABASE_PORT}/{self.DATABASE_NAME}")

    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
