from fastapi import Depends, FastAPI

from backend.config.enviroment import get_environment_variables
from backend.lifespan import lifespan
from backend.routers.employee_competency_router import EmployeeCompetencyRouter
from backend.routers.health import health_check
from backend.utils.tag import Tags

env = get_environment_variables()

app = FastAPI(
    tittle=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
    lifespan=lifespan
)