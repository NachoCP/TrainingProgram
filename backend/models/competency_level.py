import uuid

from sqlalchemy import UUID, Column, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta
from backend.utils.vocabulary import RequiredLevelEnum


class CompetencyLevel(EntityMeta):
    __tablename__ = "rules"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    competency_id = Column(UUID, ForeignKey("competency.competency_id"), nullable=False)
    required_level = Column(Enum(RequiredLevelEnum), nullable=False)
    num_workers = Column(Integer, nullable=False)

    # Relationships
    competency = relationship("Competency", back_populates="rules")
