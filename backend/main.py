from fastapi import FastAPI

from backend.config.enviroment import get_environment_variables
from backend.lifespan import lifespan
from backend.routers.api import router

env = get_environment_variables()

app = FastAPI(
    version=env.API_VERSION,
    lifespan=lifespan
)

app.include_router(router)
