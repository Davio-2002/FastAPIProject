from fastapi import FastAPI

from app.core.config import settings

from app.db.init_db import init_db
from app.db.init_db import populate_data

from app.api.endpoints import client
from contextlib import asynccontextmanager

from sqlalchemy import inspect
from app.db.session import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    populate_data()
    yield

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.include_router(client.router, prefix="/clients", tags=["clients"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Project!"}

@app.get("/tables")
def check_tables():
    inspector = inspect(engine)
    return {"tables": inspector.get_table_names()}
