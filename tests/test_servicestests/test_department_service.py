import os
import sys

from commons.models.core.department import Department

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

    entity = Department(id=1, name="Defense Against the Dark Arts")

    response = test_client.post(
        "api/v1/department",
        json=entity.model_dump(),
    )
    assert response.status_code == 201


def test_success_return_status_code_200_list(client, department) -> None:
    test_client, _, _ = client

    response = test_client.get("api/v1/department")
    assert response.status_code == 200


def test_success_return_status_code_204_delete(client, department) -> None:
    test_client, _, _ = client

    response = test_client.delete(f"api/v1/department/id/{department[0].id}")
    assert response.status_code == 204


def test_success_return_status_code_202_update(client, department) -> None:
    test_client, _, _ = client

    entity = Department(id=1, name="Defense Against the Dark Arts")
    response = test_client.put(f"api/v1/department/id/{department[0].id}", json=entity.model_dump())
    assert response.status_code == 202


def test_success_return_status_code_201_bulk(client) -> None:
    test_client, _, _ = client

    entity = [
        Department(id=1, name="Defense Against the Dark Arts"),
        Department(id=2, name="Wild and fantastic Animals"),
    ]
    response = test_client.post("api/v1/department/bulk", json=[e.model_dump() for e in entity])
    assert response.status_code == 201
