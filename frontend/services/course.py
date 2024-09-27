from typing import Any, List

import requests

from commons.config import get_environment_variables
from commons.logging import logger
from commons.models.recommender.course import CourseMatching
from frontend.services.frontend_service import IFrontendService
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()


class CourseService(IFrontendService):

    def __init__(self):
        self._base_url = f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.course.value}"

    def send_bulk(self, data: List[dict[str, Any]] = None) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"

        response = requests.post(url)
        if response.status_code == 201:
            logger.info("Successfully sent data! Course")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)

    def recommend_course(self, employee_id: int) -> CourseMatching:
        url = f"{self._base_url}/{BackendEndpoints.recommend_course.value}/{employee_id}"
        response = requests.get(url)
        if response.status_code == 200:
            logger.info(f"Successfully extract the recommendation for this employee {employee_id}")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)
        return CourseMatching(**response.json())
