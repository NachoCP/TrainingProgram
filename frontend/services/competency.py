from typing import Any, List

import requests

from commons.config import get_environment_variables
from frontend.services.frontend_service import IFrontendService
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()


class CompetencyService(IFrontendService):

    def __init__(self):
        self._base_url =f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.competency.value}"

    def send_bulk(self, data: List[dict[str, Any]]) -> None:
        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"

        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Successfully sent data! Competency")
            # Optional: Print the response from the server
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)
