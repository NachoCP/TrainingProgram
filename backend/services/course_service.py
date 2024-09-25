from typing import List

from pymilvus import MilvusClient
from sqlalchemy.orm import Session

from backend.repositories.milvus.course_repository import CourseRepository
from backend.repositories.sql_alchemy.employee_department_repository import EmployeeDepartmentRepository
from backend.repositories.sql_alchemy.feedback_repository import FeedbackRepository
from backend.services.competency_level_service import CompetencyLevelService
from backend.services.competency_service import CompetencyService
from backend.services.employee_competency_service import EmployeeCompetencyService
from backend.services.employee_service import EmployeeService
from commons.config import get_environment_variables
from commons.constants import (
    COURSE_DEFAULT_DIR_DATA,
    DEFAULT_EMBEDDING_MODEL,
)
from commons.embeddings.factory import EmbeddingProviderFactory
from commons.enum import EmbeddingFactory
from commons.models.core.course import Course
from commons.models.recommender.course import CourseAPPOutput, CourseMatching, CourseModelOutput
from commons.pipelines.competency import CompetencyPipeline
from commons.pipelines.course import CoursePipeline
from commons.ranking.ranking import CourseRanking

env = get_environment_variables()


class CourseService():

    def __init__(self, db: Session,
                 client: MilvusClient) -> None:
        self.competency_service = CompetencyService(db)
        self.repository = CourseRepository(client)
        self.employee_service = EmployeeService(client)
        self.feedback_repository = FeedbackRepository(db)
        self.employee_competency_service = EmployeeCompetencyService(db)
        self.competency_level_service = CompetencyLevelService(db)
        self.competency_service = CompetencyService(db)
        self.employee_department_repository = EmployeeDepartmentRepository(db)
        self._embeddign_runner = EmbeddingProviderFactory.get_provider(EmbeddingFactory.openai.value)(DEFAULT_EMBEDDING_MODEL, env.EMBEDDING_DIMENSION)

    def bulk(self) -> List[Course]:
        competency_data = self.competency_service.list()
        pipeline = CoursePipeline(competencies_data=competency_data)
        input_data = pipeline.extract(path=COURSE_DEFAULT_DIR_DATA)
        transformed_data = pipeline.transform(input_data)

        return self.repository.bulk([d for d in transformed_data if d is not None])

    def _convert_model_to_app_output(self,
                                     course_model_output: CourseModelOutput) -> CourseAPPOutput:
        # Convertir el objeto CourseModelOutput a un diccionario
        course_model_dict = course_model_output.model_dump()

        if "query_embedding" in course_model_dict:
            del course_model_dict["query_embedding"]

        # Crear una instancia de CourseAPPOutput con el diccionario resultante
        return CourseAPPOutput(**course_model_dict)

    def recommend_courses(self,
                          id: id) -> CourseMatching:
        department_id = self.employee_department_repository.get_id_by_employee_id(id)

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
        ranking = CourseRanking()
        input_data = ",".join(c.matching_competencies for c  in competencies_output)
        query_embedding = self._embeddign_runner.get_embedding(input_data)
        results = self.repository.search(query_embedding)
        competencies_priority = {c.matching_competencies: c.priority for c in competencies_output}
        scoring_results = ranking.scoring(competencies_priority, results)
        courses_sorted = ranking.ordering(scoring_results)
        return CourseMatching(courses=[self._convert_model_to_app_output(course) for course in courses_sorted],
                       priority=competencies_output)
