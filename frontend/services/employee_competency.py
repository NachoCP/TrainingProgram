import random
from typing import Dict, List

import requests

from commons.config import get_environment_variables
from commons.enum import RequiredLevelEnum
from commons.models.core.employee_competency import EmployeeCompetencyWithoutDates
from frontend.services.frontend_service import IFrontendService
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()

LEVEL_PROBABLITIES = {
        RequiredLevelEnum.basic: 0.5,
        RequiredLevelEnum.intermediate: 0.3,
        RequiredLevelEnum.advanced: 0.15,
        RequiredLevelEnum.expert: 0.05
    }


class EmployeeCompetencyService(IFrontendService):

    def __init__(self):
        self._base_url =f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.employee_competency.value}"


    def assign_random_level(self):
        levels = list(LEVEL_PROBABLITIES.keys())
        probabilities = list(LEVEL_PROBABLITIES.values())
        return random.choices(levels, probabilities)[0]

    def generate_employee_competencies(self,
                                       employee_ids: List[int],
                                       competency_ids: List[int]) -> List[EmployeeCompetencyWithoutDates]:
        employee_competency_data = []
        id_num = 1
        for employee in employee_ids:
            for competency in competency_ids:
                level = self.assign_random_level()
                employee_competency_data.append(EmployeeCompetencyWithoutDates(id = id_num,
                                               employee_id = employee,
                                               competency_id=competency,
                                               current_level=level.value))
                id_num += 1

        return employee_competency_data

    def send_bulk(self,
                  competency_ids: List[int],
                  employee_ids: List[int]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"
        
        data = self.generate_employee_competencies(employee_ids,
                                                   competency_ids)
        print(data)
        response = requests.post(url, json=[d.model_dump() for d in data[:10]])
        if response.status_code == 200:
            print("Successfully sent data! Employee Competency")
            # Optional: Print the response from the server
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)
