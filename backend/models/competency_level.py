from sqlalchemy import Column, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta
from commons.enum import RequiredLevelEnum


class CompetencyLevel(EntityMeta):
    __tablename__ = "competency_level"

    id = Column(Integer, primary_key=True, autoincrement=True)
    competency_id = Column(Integer, ForeignKey("competency.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
    required_level = Column(Enum(RequiredLevelEnum), nullable=False)
    num_workers = Column(Integer, nullable=False)

    # Relationships
    competency = relationship("Competency", back_populates="competency_level")
    department = relationship("Department", back_populates="competency_level")
