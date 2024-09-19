from sqlalchemy.orm import Session

from backend.models.department import Department
from backend.repositories.sql_alchemy.base_repository import BaseRepository


class DepartmenteRepository(BaseRepository[Department, int]):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
