from typing import List

from sqlalchemy.orm import Session

from backend.models.feedback import Feedback
from commons.interfaces.repository import IRepository


class FeedbackRepository(IRepository[Feedback, id]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, instance: Feedback) -> Feedback:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: id) -> Feedback:
        return self.db.get(Feedback, id)

    def get_all_by_employee(self, employee_id: int) -> List[Feedback]:
        feedbacks = self.db.query(Feedback).filter_by(employee_id=employee_id).all()
        return feedbacks

    def list(self, limit: int, start: int) -> List[Feedback]:
        return self.db.query(Feedback).offset(start).limit(limit).all()

    def update(self, id: id, instance: Feedback) -> Feedback:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: id) -> None:
        instance = self.get(id)
        if instance:
            self.db.delete(instance)
            self.db.commit()

    def bulk(self, instances: List[Feedback]) -> List[Feedback]:

        self.db.bulk_save_objects(instances)
        self.db.commit()
        return instances
