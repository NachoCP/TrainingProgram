from typing import Generic, List, TypeVar

from fastapi import Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.repositories.base_repository import BaseRepository

M = TypeVar("M")  # Model Type
K = TypeVar("K")  # Key Type (e.g., ID)

class EntityRepository(Generic[M, K], BaseRepository[M, K]):
    """
    General repository that implements BaseRepository for CRUD operations
    but allows custom methods to be defined in child classes.
    """

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:  # noqa: B008
        self.db = db

    def create(self, instance: M) -> M:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get(self, id: K) -> M:
        return self.db.get(M, id)

    def list(self, limit: int, start: int) -> List[M]:
        return self.db.query(M).offset(start).limit(limit).all()

    def update(self, id: K, instance: M) -> M:
        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance

    def delete(self, id: K) -> None:
        instance = self.get(id)
        self.db.delete(instance)
        self.db.commit()
