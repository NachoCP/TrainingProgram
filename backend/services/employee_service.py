from typing import List

from sqlalchemy.orm import Session

from backend.models.employee import Employee
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from backend.repositories.sql_alchemy.employee_repository import EmployeeRepository
from backend.repositories.sql_alchemy.feedback_repository import FeedbackRepository
from backend.services.competency_level_service import CompetencyLevelService
from backend.services.competency_service import CompetencyService
from backend.services.employee_competency_service import EmployeeCompetencyService
from commons.interfaces.service import IService
from commons.models.core.employee import Employee as EmployeeSchema
from commons.models.recommender.course import CourseModelOutput
from commons.pipelines.competency import CompetencyPipeline
from commons.recommender.recommender import CourseRecommender


class EmployeeService(IService[Employee, EmployeeSchema]):

    def __init__(self, db: Session) -> None:
        self.repository = EmployeeRepository(db)
        self.feedback_repository = FeedbackRepository(db)
        self.employee_competency_service = EmployeeCompetencyService(db)
        self.competency_level_service = CompetencyLevelService(db)
        self.competency_service = CompetencyService(db)
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
                          id: id) -> List[CourseModelOutput]:
        department_id = self.employee_department_repository.get_id_by_employee(id)

        # Extracting all the data from the different services

        feedback_reviews = self.feedback_repository.get_all_by_employee(id)
        company_competency_level = self.competency_level_service.get_all_by_department(department_id)
        department_competency_level = self.employee_competency_service.group_competency_level_by_employee_ids(department_id)
        employee_competency = self.employee_competency_service.get_all_by_employee(id)
        competency_data = self.competency_service.list()

        # Calculate the competencies to improve
        pipeline = CompetencyPipeline(competency_data)
        competencies_output = pipeline.transform(feedback_reviews=feedback_reviews,
                                       company_competency_level=company_competency_level,
                                       department_competency_level=department_competency_level,
                                       employee_competency=employee_competency)

        # Recommender algorithm
        recommender = CourseRecommender()
        input_data = ",".join(c.matching_competencies for c  in competencies_output)
        results = recommender.candidate_generation(input_data)
        competencies_priority = {c.matching_competencies: c.priority for c in competencies_output}
        scoring_results = recommender.scoring(competencies_priority, results)
        return recommender.ordering(scoring_results)
