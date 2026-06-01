from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    github_token: str = ""
    redis_url: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"


settings = Settings()