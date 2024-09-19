from pydantic import UUID4
from sqlalchemy.orm import Session

from backend.models.competency import Competency
from backend.repositories.sql_alchemy.base_repository import BaseRepository


class CompetencyRepository(BaseRepository[Competency, UUID4]):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
