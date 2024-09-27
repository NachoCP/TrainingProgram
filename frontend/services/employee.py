from typing import Any, List

import requests

from commons.config import get_environment_variables
from commons.logging import logger
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
        if response.status_code == 201:
            logger.info("Successfully sent data! Employees")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)

    def get_list_by_department(self, department_id: int) -> List[EmployeeWithoutDates]:
        url = f"{self._base_url}/{BackendEndpoints.department.value}/{department_id}"
        response = requests.get(url)
        if response.status_code == 201:
            logger.info(f"Successfully get all the employees for this departmet {department_id}")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)
        return [EmployeeWithoutDates(**r) for r in response.json()]

    def get_list(self) -> List[Employee]:
        response = requests.get(self._base_url)
        if response.status_code == 201:
            logger.info("Successfully get all the employees")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)
        return [Employee(**r) for r in response.json()]
