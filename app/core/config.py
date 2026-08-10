
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OLLAMA_MODEL: str = "qwen2.5:3b"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    DATABASE_URL: str = "postgresql://postgres:123456@localhost:5432/genai_db"

    class Config:
        env_file = ".env"


settings = Settings()

print("DATABASE URL:", settings.DATABASE_URL)