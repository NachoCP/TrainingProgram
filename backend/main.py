from fastapi import FastAPI

from backend.lifespan import lifespan
from backend.routers.api import router
from commons.config import get_environment_variables

env = get_environment_variables()

app = FastAPI(
    version=env.API_VERSION,
    lifespan=lifespan
)

app.include_router(router)
