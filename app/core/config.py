from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    APP_NAME: str = "FastAPIProject"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
