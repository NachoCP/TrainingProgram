import os
import sys

from commons.models.core.employee_department import EmployeeDepartment

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.test_servicestests.fixtures import (
    competency,
    competency_level,
    course,
    department,
    employee,
    employee_competency,
    employee_department,
    feedback,
)


def test_success_return_status_code_201_create(client, employee, department) -> None:
    test_client, _, _ = client

    entity = EmployeeDepartment(id=1, employee_id=1, department_id=1)

    response = test_client.post(
        "api/v1/employee_department",
        json=entity.model_dump(),
    )
    assert response.status_code == 201


def test_success_return_status_code_200_list(client, employee, department, employee_department) -> None:
    test_client, _, _ = client

    response = test_client.get("api/v1/employee_department")
    assert response.status_code == 200


def test_success_return_status_code_204_delete(client, employee, department, employee_department) -> None:
    test_client, _, _ = client

    response = test_client.delete(f"api/v1/employee_department/id/{department[0].id}")
    assert response.status_code == 204


def test_success_return_status_code_202_update(client, employee, department, employee_department) -> None:
    test_client, _, _ = client

    entity = EmployeeDepartment(id=1, employee_id=1, department_id=1)
    response = test_client.put(f"api/v1/employee_department/id/{department[0].id}", json=entity.model_dump())
    assert response.status_code == 202


def test_success_return_status_code_201_bulk(client) -> None:
    test_client, _, _ = client

    entity = [
        EmployeeDepartment(id=1, employee_id=1, department_id=1),
        EmployeeDepartment(id=2, employee_id=2, department_id=1),
        EmployeeDepartment(id=3, employee_id=3, department_id=2),
    ]
    response = test_client.post("api/v1/employee_department/bulk", json=[e.model_dump() for e in entity])
    assert response.status_code == 201
