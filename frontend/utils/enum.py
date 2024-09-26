from enum import Enum


class BackendEndpoints(str, Enum):
    bulk = "bulk"
    department = "department"
    employee = "employee"
    group_department = "group/department"
    recommend_course = "recommend_course"


class RouterEndpoint(str, Enum):
    competency_level = "competency_level"
    competency = "competency"
    course = "course"
    department = "department"
    feedback = "feedback"
    employee_competency = "employee_competency"
    employee_department = "employee_department"
    employee = "employee"

class ViewEnum(str, Enum):
    company_view = "company_view"
    strong_entities_view = "strong_entities_view"
    weak_entities_view = "weak_entities_view"
    employee_view = "employee_view"
