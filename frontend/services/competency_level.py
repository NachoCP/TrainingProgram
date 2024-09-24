from typing import List

import requests

from commons.config import get_environment_variables
from commons.models.core.competency_level import CompetencyLevel, CompetencyLevelOutput
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
                    "For each department generate at least 4 competencies in intermediate, 2 in advanced, 1 in expert"
                    "There is no need for basic levels"
                    f"List of departments: {department_ids}"
                    f"List of competencies: {competency_ids}"
                    "Generate a total of 40 outputs minimum")

        data = DataSyntheticLLM(CompetencyLevel).create(num=40, preamble=preamble)
        response = requests.post(url, json=[d.model_dump() for d in data])
        if response.status_code == 200:
            print("Successfully sent data! Competency Level")
            # Optional: Print the response from the server
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)

    def get_all_by_department(self,
                              department_id: int) -> List[CompetencyLevelOutput]:
        url = f"{self._base_url}/{BackendEndpoints.department.value}/{department_id}"
        response = requests.get(url)
        print(response.json())
        return [CompetencyLevelOutput(**r) for r in response.json()]

