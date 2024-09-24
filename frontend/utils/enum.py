from enum import Enum


class BackendEndpoints(str, Enum):
    bulk = "bulk"


class RouterEndpoint(str, Enum):
    competency_level = "competency_level"
    competency = "competency"
    course = "course"
    department = "department"
    feedback = "feedback"
    employee_competency = "employee_competency"
    employee_department = "employee_department"
    employee = "employee"
