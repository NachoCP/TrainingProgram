from fastapi import APIRouter

from backend.routers.v1 import (
    competency_level_router,
    competency_router,
    course_router,
    department_router,
    employee_competency_router,
    employee_department_router,
    employee_router,
    health,
)

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(competency_level_router.router)
router.include_router(competency_router.router)
router.include_router(course_router.router)
router.include_router(department_router.router)
router.include_router(employee_competency_router.router)
router.include_router(employee_department_router.router)
router.include_router(employee_router.router)
router.include_router(health.router)
