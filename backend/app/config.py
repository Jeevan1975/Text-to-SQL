from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    SUPABASE_HOST: str
    SUPABASE_PORT: int
    SUPABASE_PASSWORD: str
    SUPABASE_USER: str
    GOOGLE_API_KEY: str
    ENV: str = "dev"
    
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent.parent / ".env")
    )  


settings = Settings()