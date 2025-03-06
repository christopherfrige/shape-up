from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database settings
    db_driver: str = "postgresql"
    db_user: str = "postgres"
    db_password: str = "password"
    db_host: str = "localhost"
    db_port: str = "5432"
    db_name: str = "shape_up"

    # JWT settings
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    app_environment: str = "development"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


SETTINGS = get_settings()
