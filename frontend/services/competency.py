from typing import Any, List

import requests

from commons.config import get_environment_variables
from commons.logging import logger
from commons.models.core.competency import Competency
from frontend.services.frontend_service import IFrontendService
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()


class CompetencyService(IFrontendService):

    def __init__(self):
        self._base_url = f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.competency.value}"

    def send_bulk(self, data: List[dict[str, Any]]) -> None:
        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"

        response = requests.post(url, json=data)
        if response.status_code == 201:
            logger.info("Successfully sent data! Competency")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)

    def get_list(self) -> List[Competency]:

        response = requests.get(self._base_url)
        if response.status_code == 200:
            logger.info(f"Successfully extracted all the competencies {len(response.json())}")
        else:
            logger.info(f"Failed to send data. Status code: {response.status_code}")
            logger.info(response.text)
        return [Competency(**r) for r in response.json()]
