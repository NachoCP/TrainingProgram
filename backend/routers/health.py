from fastapi import APIRouter

HealthRouter = APIRouter(prefix="/health", tags=["health"])

@HealthRouter.get("/health", status_code=200)
def health_check() -> dict:
    """
    Checks the health of the project.

    It returns 200 status if the project is healthy.
    """
    return {"status": "healthy"}
