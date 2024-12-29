from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    APP_NAME: str = "FastAPI Project"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
