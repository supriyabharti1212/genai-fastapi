
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OLLAMA_MODEL: str = "qwen2.5:3b"
    OLLAMA_BASE_URL: str = "http://localhost:11434"

    class Config:
        env_file = ".env"


settings = Settings()