from typing import Any, List

import requests

from commons.config import get_environment_variables
from commons.models.core.department import Department
from frontend.services.frontend_service import IFrontendService
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()


class DepartmentService(IFrontendService):
    def __init__(self):

        self._base_url = f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.department.value}"

    def send_bulk(self, data: List[dict[str, Any]]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"

        response = requests.post(url, json=data)
        if response.status_code == 201:
            print("Successfully sent data! Department")
            # Optional: Print the response from the server
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)

    def get_list(self) -> List[Department]:

        response = requests.get(self._base_url)
        return [Department(**r) for r in response.json()]
