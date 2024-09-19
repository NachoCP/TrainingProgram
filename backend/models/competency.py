import uuid

from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class Competency(EntityMeta):
    __tablename__ = "competency"

    competency_id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)

    # Relationships
    employees = relationship("EmployeeCompetency", back_populates="competency")
    competency_level = relationship("CompetencyLevel", back_populates="competency")
