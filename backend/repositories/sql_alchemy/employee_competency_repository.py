from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.models.employee_competency import EmployeeCompetency
from backend.repositories.sql_alchemy.base_repository import BaseRepository


class EmployeeCompetencyRepository(BaseRepository[EmployeeCompetency, UUID4]):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
