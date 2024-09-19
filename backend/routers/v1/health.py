from fastapi import APIRouter, status

router = APIRouter(
    prefix="/health",
    tags=["health"]
    )

@router.get("", status_code=status.HTTP_200_OK)
def health_check() -> dict:
    """
    Checks the health of the project.

    It returns 200 status if the project is healthy.
    """
    return {"status": "healthy"}
