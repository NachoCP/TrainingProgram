from typing import List, Optional

from fastapi import APIRouter, status

from backend.schemas.employee_competency import EmployeeCompetency
from backend.services.employee_competency_service import EmployeeCompetencyService

employee_competency_router = APIRouter(prefix="/employee-competencies", tags=["employee-competency"])




@employee_competency_router.post("/", status_code=status.HTTP_201_CREATED, response_model=EmployeeCompetency)

@employee_competency_router.get("/", response_model=List[EmployeeCompetency])
def index(
    employeeCompetencyService: EmployeeCompetencyService,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0
):
    return [
        competency.normalize()
        for competency in employeeCompetencyService.list(pageSize, startIndex)
    ]

@employee_competency_router.get("/{id}", response_model=EmployeeCompetency)
def get(id: int,
        employeeCompetencyService: EmployeeCompetencyService):
    return employeeCompetencyService.get(id).normalize()

@employee_competency_router.post("/", response_model=EmployeeCompetency, status_code=status.HTTP_201_CREATED)
def create(
    employee_competency: EmployeeCompetency,
    employeeCompetencyService: EmployeeCompetencyService):

    return employeeCompetencyService.create(employee_competency).normalize()

@employee_competency_router.patch("/{id}", response_model=EmployeeCompetency)
def update(id: int, employee_competency: EmployeeCompetency, employeeCompetencyService: EmployeeCompetencyService):
    return employeeCompetencyService.update(id, employee_competency).normalize()

@employee_competency_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, employeeCompetencyService: EmployeeCompetencyService):
    return employeeCompetencyService.delete(id)
