from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.models.base import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):

    init_db()

    yield
