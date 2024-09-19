from typing import List

from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.interfaces.repository import IRepository
from backend.models.department import Department


class DepartmenteRepository(IRepository[Department, UUID4]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, instance: Department) -> Department:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: UUID4) -> Department:
        return self.db.get(Department, id)

    def list(self, limit: int, start: int) -> List[Department]:
        return self.db.query(Department).offset(start).limit(limit).all()

    def update(self, id: UUID4, instance: Department) -> Department:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: UUID4) -> None:
        instance = self.get(id)
        if instance:
            self.db.delete(instance)
            self.db.commit()
