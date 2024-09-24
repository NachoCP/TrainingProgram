from typing import List

from sqlalchemy.orm import Session

from backend.models.employee_competency import EmployeeCompetency
from backend.repositories.sql_alchemy.employee_competency_repository import EmployeeCompetencyRepository
from commons.interfaces.service import IService
from commons.models.core.competency_level import CompetencyLevelEmployeeOutput, CompetencyLevelOutput
from commons.models.core.employee_competency import EmployeeCompetency as EmployeeCompetencySchema


class EmployeeCompetencyService(IService[EmployeeCompetency, EmployeeCompetencySchema]):

    def __init__(self, db: Session) -> None:
        self.repository = EmployeeCompetencyRepository(db)

    def create(self, schema: EmployeeCompetencySchema) -> EmployeeCompetency:
        employee_competency = EmployeeCompetency(**schema.model_dump(exclude_none=True))
        return self.repository.create(employee_competency)

    def delete(self, id: id) -> None:
        self.repository.delete(id)

    def get(self, id: id) -> EmployeeCompetency:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[EmployeeCompetency]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: id, schema: EmployeeCompetencySchema) -> EmployeeCompetency:
        employee_competency = EmployeeCompetency(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, employee_competency)

    def bulk(self, schemas: List[EmployeeCompetencySchema]) -> List[EmployeeCompetency]:
        schema_objects = [EmployeeCompetency(**schema.model_dump(exclude_none=True)) for schema in schemas]
        return self.repository.bulk(schema_objects)

    def get_all_by_department(self, department_id: int) -> List[CompetencyLevelEmployeeOutput]:
        return [CompetencyLevelEmployeeOutput(**d) for d in self.repository.get_all_by_department(department_id)]

    def get_all_by_employee(self, employee_id: id) -> List[CompetencyLevelEmployeeOutput]:
        return [CompetencyLevelEmployeeOutput(**d) for d in self.repository.get_all_by_employee(employee_id)]

    def group_competency_level_by_employee_ids(self, department_id: id) -> List[CompetencyLevelOutput]:
        return [CompetencyLevelOutput(**d) for d in self.repository.group_competency_level_by_employee_ids(department_id)]
