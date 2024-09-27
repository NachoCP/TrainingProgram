import os
import sys

from commons.models.core.competency import Competency

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

    entity = Competency(id=1, name="Dark Arts", description="Lorem Ipsum")

    response = test_client.post(
        "api/v1/competency",
        json=entity.model_dump(),
    )
    assert response.status_code == 201


def test_success_return_status_code_200_list(client, competency) -> None:
    test_client, _, _ = client

    response = test_client.get("api/v1/competency")
    assert response.status_code == 200


def test_success_return_status_code_204_delete(client, competency) -> None:
    test_client, _, _ = client

    response = test_client.delete(f"api/v1/competency/id/{competency[0].id}")
    assert response.status_code == 204


def test_success_return_status_code_202_update(client, competency) -> None:
    test_client, _, _ = client

    entity = Competency(id=1, name="Dark Arts", description="Lorem Ipsum")
    response = test_client.put(f"api/v1/competency/id/{competency[0].id}", json=entity.model_dump())
    assert response.status_code == 202


def test_success_return_status_code_201_bulk(client) -> None:
    test_client, _, _ = client

    entity = [
        Competency(id=1, name="Dark Arts", description="Lorem Ipsum"),
        Competency(id=2, name="Potions", description="Lorem Ipsum"),
    ]
    response = test_client.post("api/v1/competency/bulk", json=[e.model_dump() for e in entity])
    assert response.status_code == 201
