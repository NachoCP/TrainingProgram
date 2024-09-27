from typing import Any, List

import requests

from commons.config import get_environment_variables
from commons.logging import logger
from commons.models.core.competency_level import CompetencyLevelOutput
from frontend.services.frontend_service import IFrontendService
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()


class CompetencyLevelService(IFrontendService):

    def __init__(self):
        self._base_url = (
            f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.competency_level.value}"
        )

    def send_bulk(self, data: List[dict[str, Any]]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"

        response = requests.post(url, json=data)
        if response.status_code == 201:
            logger.info("Successfully sent data! Competency Level")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)

    def get_all_by_department(self, department_id: int) -> List[CompetencyLevelOutput]:
        url = f"{self._base_url}/{BackendEndpoints.department.value}/{department_id}"
        response = requests.get(url)
        if response.status_code == 200:
            logger.info("Successfully get all the competency data from the department")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)
        return [CompetencyLevelOutput(**r) for r in response.json()]
