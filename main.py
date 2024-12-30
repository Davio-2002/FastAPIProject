from fastapi import FastAPI
from app.core.config import settings
from app.db.init_db import init_db
from app.db.session import engine
from sqlalchemy import inspect

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to David's FastAPI Project!"}

@app.get("/tables")
def check_tables():
    inspector = inspect(engine)
    return {"tables": inspector.get_table_names()}
