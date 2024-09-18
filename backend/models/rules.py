from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta
from backend.utils.vocabulary import RequiredLevelEnum


class Rules(EntityMeta):
    __tablename__ = 'rules'

    id = Column(Integer, primary_key=True)
    competency_id = Column(Integer, ForeignKey('competency.competency_id'), nullable=False)
    required_level = Column(Enum(RequiredLevelEnum), nullable=False)
    num_persona = Column(Integer, nullable=False)
    company_level = Column(String, nullable=False)
    set_by_id = Column(Integer, nullable=False)

    # Relationships
    competency = relationship("Competency", back_populates="rules")
