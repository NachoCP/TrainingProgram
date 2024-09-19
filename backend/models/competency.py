import uuid

from sqlalchemy import UUID, Column, Enum, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta
from backend.utils.vocabulary import TypeEnum


class Competency(EntityMeta):
    __tablename__ = "competency"

    competency_id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    type = Column(Enum(TypeEnum), nullable=False)
    description = Column(String)

    # Relationships
    employees = relationship("EmployeeCompetency", back_populates="competency")
    rules = relationship("Rules", back_populates="competency")
