import os
import sys

from commons.models.core.employee import Employee

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.fixtures import (
    competency,
    competency_level,
    course,
    department,
    employee,
    employee_competency,
    employee_department,
    feedback,
)


def test_success_return_status_code_201_create(client) -> None:
    test_client, _, _ = client

    entity = Employee(id=1, name="Gandalf the White")

    response = test_client.post(
        "api/v1/employee",
        json=entity.model_dump(),
    )
    assert response.status_code == 201


def test_success_return_status_code_200_list(client, employee) -> None:
    test_client, _, _ = client

    response = test_client.get("api/v1/employee")
    assert response.status_code == 200


def test_success_return_status_code_204_delete(client, employee) -> None:
    test_client, _, _ = client

    response = test_client.delete(f"api/v1/employee/id/{employee[0].id}")
    assert response.status_code == 204


def test_success_return_status_code_202_update(client, employee) -> None:
    test_client, _, _ = client

    entity = Employee(id=1, name="Gandalf the Grey")
    response = test_client.put(f"api/v1/employee/id/{employee[0].id}", json=entity.model_dump())
    assert response.status_code == 202


def test_success_return_status_code_201_bulk(client) -> None:
    test_client, _, _ = client

    entity = [
        Employee(id=1, name="Gandalf the White"),
        Employee(id=2, name="Saruman of Many Colours"),
        Employee(id=3, name="Radagast the Green"),
    ]
    response = test_client.post("api/v1/employee/bulk", json=[e.model_dump() for e in entity])
    assert response.status_code == 201


def test_success_return_status_code_201_get_department(client, employee, department, employee_department) -> None:
    test_client, _, _ = client

    response = test_client.get(f"api/v1/employee/department/{employee[0].id}")
    assert response.status_code == 202
