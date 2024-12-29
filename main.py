from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to FastAPI Project!",
        "database_url": settings.DATABASE_URL,
        "debug": settings.DEBUG
    }
