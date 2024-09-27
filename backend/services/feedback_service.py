from typing import List

from sqlalchemy.orm import Session

from backend.models.feedback import Feedback
from backend.repositories.sql_alchemy.feedback_repository import FeedbackRepository
from commons.interfaces.service import IService
from commons.logging import logger
from commons.models.core.feedback import Feedback as FeedbackSchema


class FeedbackService(IService[Feedback, FeedbackSchema]):

    def __init__(self, db: Session) -> None:
        self.repository = FeedbackRepository(db)

    def create(self, schema: FeedbackSchema) -> Feedback:
        feedback = Feedback(**schema.model_dump(exclude_none=True))
        return self.repository.create(feedback)

    def delete(self, id: id) -> None:
        self.repository.delete(id)

    def get(self, id: id) -> Feedback:
        return self.repository.get(id)

    def list(self, pageSize: int = 100, startIndex: int = 0) -> List[Feedback]:
        return self.repository.list(pageSize, startIndex)

    def update(self, id: id, schema: FeedbackSchema) -> Feedback:
        feedback = Feedback(**schema.model_dump(exclude_none=True))
        return self.repository.update(id, feedback)

    def bulk(self, schemas: List[FeedbackSchema]) -> List[Feedback]:
        logger.info(f"Dumping the following number of feedbacks {len(schemas)}")
        schema_objects = [Feedback(**schema.model_dump(exclude_none=True)) for schema in schemas]
        return self.repository.bulk(schema_objects)

    def get_all_by_employee(self, employee_id: id) -> List[Feedback]:
        logger.info(f"Getting all the feedbacks from the following employee {employee_id}")
        return self.repository.get_all_by_employee(employee_id)
