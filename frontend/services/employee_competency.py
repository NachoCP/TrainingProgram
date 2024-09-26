from typing import Any, List

import requests

from commons.config import get_environment_variables
from commons.enum import RequiredLevelEnum
from commons.models.core.competency_level import CompetencyLevelEmployeeOutput, CompetencyLevelOutput
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

    def send_bulk(self, data: List[dict[str, Any]]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"

        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Successfully sent data! Employee Competency")
            # Optional: Print the response from the server
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)

    def get_all_by_department(self,
                              department_id: int) -> List[CompetencyLevelEmployeeOutput]:
        url = f"{self._base_url}/{BackendEndpoints.department.value}/{department_id}"
        response = requests.get(url)
        return [CompetencyLevelEmployeeOutput(**r) for r in response.json()]

    def get_all_group_department(self,
                                 department_id: int) -> List[CompetencyLevelOutput]:

        url = f"{self._base_url}/{BackendEndpoints.group_department.value}/{department_id}"
        response = requests.get(url)
        return [CompetencyLevelOutput(**r) for r in response.json()]

    def get_all_by_employee(self,
                            employee_id: int) -> List[CompetencyLevelEmployeeOutput]:
        url = f"{self._base_url}/{BackendEndpoints.employee.value}/{employee_id}"
        response = requests.get(url)
        return [CompetencyLevelEmployeeOutput(**r) for r in response.json()]
