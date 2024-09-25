from config.database import engine

from backend.models.base import Base
from backend.models.competency import Competency
from backend.models.competency_level import CompetencyLevel
from backend.models.department import Department
from backend.models.employee import Employee
from backend.models.employee_competency import EmployeeCompetency
from backend.models.employee_department import EmployeeDepartment
from backend.models.feedback import Feedback


def create_tables():
    Base.metadata.drop_all(bind=engine)
    Competency.metadata.drop_all(bind=engine)
    Employee.metadata.drop_all(bind=engine)
    Department.metadata.drop_all(bind=engine)
    CompetencyLevel.metadata.drop_all(bind=engine)
    EmployeeCompetency.metadata.drop_all(bind=engine)
    EmployeeDepartment.metadata.drop_all(bind=engine)
    Feedback.metadata.drop_all(bind=engine)
