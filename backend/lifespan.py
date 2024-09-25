from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.utils.drop_tables import drop_tables
from backend.utils.init_db import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):

    create_tables()
    yield
    drop_tables()
