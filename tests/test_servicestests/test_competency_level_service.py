import os
import sys

from commons.models.core.competency_level import CompetencyLevel

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from commons.enum import RequiredLevelEnum
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


def test_success_return_status_code_201_create(client, competency, department) -> None:
    test_client, _, _ = client

    entity = CompetencyLevel(
        id=2, competency_id=2, department_id=1, required_level=RequiredLevelEnum.intermediate.value, num_workers=8
    )

    response = test_client.post(
        "api/v1/competency_level",
        json=entity.model_dump(),
    )
    assert response.status_code == 201


def test_success_return_status_code_200_list(client, competency, department, competency_level) -> None:
    test_client, _, _ = client

    response = test_client.get("api/v1/competency_level")
    assert response.status_code == 200


def test_success_return_status_code_204_delete(client, competency, department, competency_level) -> None:
    test_client, _, _ = client

    response = test_client.delete(f"api/v1/competency_level/id/{competency_level[0].id}")
    assert response.status_code == 204


def test_success_return_status_code_202_update(client, competency, department, competency_level) -> None:
    test_client, _, _ = client

    entity = CompetencyLevel(
        id=2, competency_id=2, department_id=1, required_level=RequiredLevelEnum.intermediate.value, num_workers=8
    )
    response = test_client.put(f"api/v1/competency_level/id/{competency_level[0].id}", json=entity.model_dump())
    assert response.status_code == 202


def test_success_return_status_code_201_bulk(client) -> None:
    test_client, _, _ = client

    entity = [
        CompetencyLevel(
            id=1, competency_id=1, department_id=1, required_level=RequiredLevelEnum.advanced.value, num_workers=5
        ),
        CompetencyLevel(
            id=2, competency_id=2, department_id=1, required_level=RequiredLevelEnum.intermediate.value, num_workers=8
        ),
    ]
    response = test_client.post("api/v1/competency_level/bulk", json=[e.model_dump() for e in entity])
    assert response.status_code == 201


def test_success_return_status_code_202_get_department(client, competency, department, competency_level) -> None:
    test_client, _, _ = client

    response = test_client.get(f"api/v1/competency_level/department/{competency_level[0].department_id}")
    assert response.status_code == 200
