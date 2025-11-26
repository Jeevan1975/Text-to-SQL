from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SUPABASE_HOST: str
    SUPABASE_PORT: str
    SUPABASE_PASSWORD: str
    GOOGLE_API_KEY: str
    ENV: str = "dev"
    
    class Config():
        env_file = ".env"
    

settings = Settings()