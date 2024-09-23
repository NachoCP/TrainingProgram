from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.models.base import EntityMeta


class Feedback(EntityMeta):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    feedback_by = Column(Integer, ForeignKey("employee.id"), nullable=False)
    comments = Column(String, nullable=False)
    score = Column(Float, nullable=True)
    effective_date = Column(String, nullable=False)

    # Relationships
    employee = relationship("Employee", foreign_keys=[employee_id], back_populates="feedback_received")
    feedback_giver = relationship("Employee", foreign_keys=[feedback_by], back_populates="feedback_given")
