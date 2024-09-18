from fastapi import Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db_connection
from backend.models.rules import Rules
from backend.repositories.sql_alchemy.entity_repository import BaseRepository


class RulesRepository(BaseRepository[Rules, int]):
    def __init__(self, db: Session = Depends(get_db_connection)) -> None:  # noqa: B008
        super().__init__(db)
