from typing import List

from sqlalchemy.orm import Session

from backend.interfaces.repository import IRepository
from backend.models.employee_department import EmployeeDepartment


class EmployeeDepartmentRepository(IRepository[EmployeeDepartment, id]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, instance: EmployeeDepartment) -> EmployeeDepartment:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: id) -> EmployeeDepartment:
        return self.db.get(EmployeeDepartment, id)

    def list(self, limit: int, start: int) -> List[EmployeeDepartment]:
        return self.db.query(EmployeeDepartment).offset(start).limit(limit).all()

    def update(self, id: id, instance: EmployeeDepartment) -> EmployeeDepartment:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: id) -> None:
        instance = self.get(id)
        if instance:
            self.db.delete(instance)
            self.db.commit()
