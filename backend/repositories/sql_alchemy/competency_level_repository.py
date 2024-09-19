from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.models.competency_level import CompetencyLevel
from backend.repositories.sql_alchemy.base_repository import BaseRepository


class CompetencyLevelRepository(BaseRepository[CompetencyLevel, UUID4]):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
