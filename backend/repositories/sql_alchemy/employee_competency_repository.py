from fastapi import Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.models.employee_competency import EmployeeCompetency
from backend.repositories.sql_alchemy.entity_repository import BaseRepository


class EmployeeCompetencyRepository(BaseRepository[EmployeeCompetency, int]):
    def __init__(self, db: Session = Depends(get_db_connection)) -> None:  # noqa: B008
        super().__init__(db)
