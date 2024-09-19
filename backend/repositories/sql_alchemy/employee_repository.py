from typing import List

from sqlalchemy.orm import Session

from backend.interfaces.repository import IRepository
from backend.models.employee import Employee


class EmployeeRepository(IRepository[Employee, id]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, instance: Employee) -> Employee:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: id) -> Employee:
        return self.db.get(Employee, id)

    def list(self, limit: int, start: int) -> List[Employee]:
        return self.db.query(Employee).offset(start).limit(limit).all()

    def update(self, id: id, instance: Employee) -> Employee:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: id) -> None:
        instance = self.get(id)
        if instance:
            self.db.delete(instance)
            self.db.commit()
