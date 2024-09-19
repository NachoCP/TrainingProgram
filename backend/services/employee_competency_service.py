from typing import List

from backend.interfaces.service import IService
from backend.models.employee_competency import EmployeeCompetency
from backend.repositories.sql_alchemy.employee_competency_repository import EmployeeCompetencyRepository
from backend.schemas.employee_competency import EmployeeCompetency as EmployeeCompetencySchema


class EmployeeCompetencyService(IService[EmployeeCompetency, EmployeeCompetencySchema]):
    def __init__(self, employeeCompetencyRepository: EmployeeCompetencyRepository) -> None:
        self.employeeCompetencyRepository = employeeCompetencyRepository

    def create(self, schema: EmployeeCompetencySchema) -> EmployeeCompetency:
        employee_competency = EmployeeCompetency(**schema.model_dump(exclude_none=True))
        return self.employeeCompetencyRepository.create(employee_competency)

    def delete(self, id: int) -> None:
        self.employeeCompetencyRepository.delete(id)

    def get(self, id: int) -> EmployeeCompetency:
        return self.employeeCompetencyRepository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[EmployeeCompetency]:
        return self.employeeCompetencyRepository.list(pageSize, startIndex)

    def update(self, id: int, schema: EmployeeCompetencySchema) -> EmployeeCompetency:
        employee_competency = EmployeeCompetency(**schema.model_dump(exclude_none=True))
        return self.employeeCompetencyRepository.update(id, employee_competency)
