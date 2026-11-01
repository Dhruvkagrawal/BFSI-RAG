from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "bfsi-rag"
    api_v1_prefix: str = "/api/v1"
    gemini_api_key: str
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()