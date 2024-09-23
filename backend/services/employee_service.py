from typing import List

from sqlalchemy.orm import Session

from backend.models.competency_level import CompetencyLevel
from backend.models.employee import Employee
from backend.models.employee_competency import EmployeeCompetency
from backend.models.employee_department import EmployeeDepartment
from backend.models.feedback import Feedback
from backend.repositories.sql_alchemy.competency_level_repository import CompetencyLevelRepository
from backend.repositories.sql_alchemy.competency_repository import CompetencyRepository
from backend.repositories.sql_alchemy.employee_competency_repository import EmployeeCompetencyRepository
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository
from backend.repositories.sql_alchemy.feedback_repository import FeedbackRepository
from commons.enum import required_level_weights
from commons.interfaces.service import IService
from commons.models.core.employee import Employee as EmployeeSchema
from commons.models.recommender.course import CourseModelOutput
from commons.recommender.recommender import CourseRecommender


class EmployeeService(IService[Employee, EmployeeSchema]):

    def __init__(self, db: Session) -> None:
        self.repository = EmployeeRepository(db)
        self.feedback_repository = FeedbackRepository(db)
        self.employee_competency_repository = EmployeeCompetencyRepository(db)
        self.competency_level_repository = CompetencyLevelRepository(db)
        self.employee_department_repository = EmployeeDepartmentRepository(db)

    def create(self, schema: EmployeeSchema) -> Employee:
        employee = Employee(**schema.model_dump(exclude_none=True))
        return self.repository.create(employee)

    def delete(self, id: id) -> None:
        self.repository.delete(id)

    def get(self, id: id) -> Employee:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Employee]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: id, schema: EmployeeSchema) -> Employee:
        employee = Employee(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, employee)

    def bulk(self, schemas: List[EmployeeSchema]) -> List[Employee]:
        schema_objects = [Employee(**schema.model_dump(exclude_none=True)) for schema in schemas]
        return self.repository.bulk(schema_objects)

    def recommend_courses(self,
                          id: id,
                          department_id: id) -> List[CourseModelOutput]:
        feedback_reviews = [Feedback.from_orn(feedback) for feedback in self.feedback_repository.get_all_by_employee(id)]

        competency_level = [CompetencyLevel.from_orn(competency_level) for competency_level in self.competency_level_repository.get_all_by_department(department_id)]

        employees = self.employee_department_repository.get_all_by_department(department_id=department_id)
        employees = [EmployeeDepartment.from_orn(employee) for employee in employees]

        competency_department_level = self.employee_competency_repository.group_competency_level_by_employee_ids([employee.employee_id for employee in employees])

        employee_competencies = [EmployeeCompetency.from_orn(employee_competency) for employee_competency in self.employee_competency_repository.get_all_by_employee(id)]

