from typing import Any, List

import requests

from commons.config import get_environment_variables
from commons.enum import RequiredLevelEnum
from commons.logging import logger
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

    def send_bulk(self, data: List[dict[str, Any]]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"

        response = requests.post(url, json=data)
        if response.status_code == 201:
            logger.info("Successfully sent data! Employee Department")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)
