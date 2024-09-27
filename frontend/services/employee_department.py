from typing import Any, Dict, List

import requests

from commons.config import get_environment_variables
from commons.enum import RequiredLevelEnum
from commons.models.core.employee_department import EmployeeDepartmentWithoutDates
from frontend.services.frontend_service import IFrontendService
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()

LEVEL_PROBABLITIES = {
    RequiredLevelEnum.basic: 0.5,
    RequiredLevelEnum.intermediate: 0.3,
    RequiredLevelEnum.advanced: 0.15,
    RequiredLevelEnum.expert: 0.05,
}


class EmployeeDepartmentService(IFrontendService):

    def __init__(self):
        self._base_url = (
            f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.employee_department.value}"
        )

    def distribute_employees(self, departments: List[str], employees: List[str]) -> Dict[str, List[str]]:
        department_assignments = []
        index = 1
        for i, employee in enumerate(employees):
            department_index = i % len(departments)
            department_assignments.append(
                EmployeeDepartmentWithoutDates(
                    id=index, employee_id=employee, department_id=departments[department_index]
                )
            )
            index += 1

        return department_assignments

    def send_bulk(self, data: List[dict[str, Any]]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"

        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Successfully sent data! Employee Department")
            # Optional: Print the response from the server
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)
