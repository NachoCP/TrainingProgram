from typing import List

from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.interfaces.service import IService
from backend.models.employee_competency import EmployeeCompetency
from backend.repositories.sql_alchemy.employee_competency_repository import EmployeeCompetencyRepository
from backend.schemas.employee_competency import EmployeeCompetency as EmployeeCompetencySchema


class EmployeeCompetencyService(IService[EmployeeCompetency, EmployeeCompetencySchema]):

    def __init__(self, db: Session) -> None:
        self.repository = EmployeeCompetencyRepository(db)

    def create(self, schema: EmployeeCompetencySchema) -> EmployeeCompetency:
        employee_competency = EmployeeCompetency(**schema.model_dump(exclude_none=True))
        return self.repository.create(employee_competency)

    def delete(self, id: UUID4) -> None:
        self.repository.delete(id)

    def get(self, id: UUID4) -> EmployeeCompetency:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[EmployeeCompetency]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: UUID4, schema: EmployeeCompetencySchema) -> EmployeeCompetency:
        employee_competency = EmployeeCompetency(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, employee_competency)
