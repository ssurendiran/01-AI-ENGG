# src/chatbot_ui/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    OPENAI_API_KEY: str | None = None
    GROQ_API_KEY: str | None = None
    GOOGLE_API_KEY: str | None = None

    # ✅ Important: define as field, not class var
    API_URL: str = "http://api:8000"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


# ✅ Create instance
config = Config()