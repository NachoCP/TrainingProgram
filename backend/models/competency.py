from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta
from backend.utils.vocabulary import TypeEnum


class Competency(EntityMeta):
    __tablename__ = 'competency'

    competency_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(Enum(TypeEnum), nullable=False)
    description = Column(String)

    # Relationships
    employees = relationship("EmployeeCompetency", back_populates="competency")
    rules = relationship("Rules", back_populates="competency")
