from typing import Any, List

import requests

from commons.config import get_environment_variables
from commons.models.core.employee import Employee, EmployeeWithoutDates
from frontend.services.frontend_service import IFrontendService
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()


class EmployeeService(IFrontendService):

    def __init__(self):
        self._base_url = f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.employee.value}"

    def send_bulk(self, data: List[dict[str, Any]]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"
        response = requests.post(url, json=data)
        if response.status_code == 202:
            print("Successfully sent data! Employee")
            # Optional: Print the response from the server
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)

    def get_list_by_department(self, department_id: int) -> List[EmployeeWithoutDates]:
        url = f"{self._base_url}/{BackendEndpoints.department.value}/{department_id}"
        response = requests.get(url)
        return [EmployeeWithoutDates(**r) for r in response.json()]

    def get_list(self) -> List[Employee]:
        response = requests.get(self._base_url)
        return [Employee(**r) for r in response.json()]
