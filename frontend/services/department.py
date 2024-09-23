from typing import Any, List

import requests

from commons.config import get_environment_variables
from frontend.services.frontend_service import IFrontendService

env = get_environment_variables()


class DepartmentService(IFrontendService):

    def send(self, data: List[dict[str, Any]]) -> None:
        url = f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/department/bulk"

        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Successfully sent data!")
            # Optional: Print the response from the server
            print(response.json())
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)
