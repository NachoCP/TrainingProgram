from sqlalchemy.orm import Session

from backend.models.competency_level import CompetencyLevel
from backend.repositories.sql_alchemy.base_repository import BaseRepository


class CompetencyLevelRepository(BaseRepository[CompetencyLevel, int]):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
