from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    github_app_id: str = ""
    github_installation_id: str = ""
    github_private_key_path: str = ""

    redis_url: str = "redis://localhost:6379"
    gemini_api_key: str
    class Config:
        env_file = ".env"


settings = Settings()