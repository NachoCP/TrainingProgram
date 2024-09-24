from typing import List

import requests

from commons.config import get_environment_variables
from commons.models.core.competency_level import CompetencyLevel
from frontend.services.frontend_service import IFrontendService
from frontend.synthetic.synthetic_llm import DataSyntheticLLM
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()


class CompetencyLevelService(IFrontendService):

    def __init__(self):
        self._base_url =f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.competency_level.value}"

    def send_bulk(self,
                  competency_ids: List[int],
                  department_ids: List[int]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"
        preamble = ("You are going to be provided with two list: competencies and departments."
                    "Used them to generate the rules to set up level of competencies between the different departments"
                    "Be realistic with the standards, there cannot be basic levels"
                    "Do not use other ids rather than the others provided"
                    f"List of departments: {department_ids}",
                    f"List of competencies: {competency_ids}")

        data = DataSyntheticLLM(CompetencyLevel).create(num=10, preamble=preamble)
        response = requests.post(url, json=[d.model_dump() for d in data])
        if response.status_code == 200:
            print("Successfully sent data! Competency Level")
            # Optional: Print the response from the server
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)
