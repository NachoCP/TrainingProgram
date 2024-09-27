from typing import Any, List

import requests

from commons.config import get_environment_variables
from commons.logging import logger
from commons.models.core.feedback import Feedback
from frontend.services.frontend_service import IFrontendService
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()


class FeedbackService(IFrontendService):

    def __init__(self):
        self._base_url = f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.feedback.value}"

    def send_bulk(self, data: List[dict[str, Any]]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"

        response = requests.post(url, json=data)
        if response.status_code == 201:
            logger.info("Successfully sent data! Feedbacks")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)

    def get_all_by_employee(self, employee_id: int) -> List[Feedback]:
        url = f"{self._base_url}/{BackendEndpoints.employee.value}/{employee_id}"
        response = requests.get(url)
        if response.status_code == 200:
            logger.info(f"Successfully get all the feedback from this employee {employee_id}")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)
        return [Feedback(**r) for r in response.json()]
