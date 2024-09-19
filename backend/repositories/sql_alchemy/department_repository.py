from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.models.department import Department
from backend.repositories.sql_alchemy.base_repository import BaseRepository


class DepartmenteRepository(BaseRepository[Department, UUID4]):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
