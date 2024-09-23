from typing import List

from pymilvus import MilvusClient
from sqlalchemy.orm import Session

from backend.repositories.milvus.course_repository import CourseRepository
from backend.services.competency_service import CompetencyService
from commons.constants import COURSE_DEFAULT_DIR_DATA
from commons.models.core.course import Course
from commons.pipelines.course import CoursePipeline


class CourseService():

    def __init__(self, db: Session,
                 client: MilvusClient) -> None:
        self.competency_service = CompetencyService(db)
        self.repository = CourseRepository(client)

    def bulk(self) -> List[Course]:
        competency_data = self.competency_service.list()
        pipeline = CoursePipeline(competencies_data=competency_data)
        input_data = pipeline.extract(path=COURSE_DEFAULT_DIR_DATA)
        transformed_data = pipeline.transform(input_data)

        return self.repository.bulk([d for d in transformed_data if d is not None])
