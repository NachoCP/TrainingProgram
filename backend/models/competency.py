from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class Competency(EntityMeta):
    __tablename__ = "competency"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)

    # Relationships
    employees = relationship("EmployeeCompetency", back_populates="competency")
    competency_level = relationship("CompetencyLevel", back_populates="competency")
