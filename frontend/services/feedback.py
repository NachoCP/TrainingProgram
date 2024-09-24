from typing import List

import requests

from commons.config import get_environment_variables
from commons.models.core.feedback import Feedback
from frontend.services.frontend_service import IFrontendService
from frontend.synthetic.synthetic_llm import DataSyntheticLLM
from frontend.utils.enum import BackendEndpoints, RouterEndpoint

env = get_environment_variables()


class FeedbackService(IFrontendService):

    def __init__(self):
        self._base_url =f"http://{env.BACKEND_HOSTNAME}:{env.BACKEND_PORT}/api/v1/{RouterEndpoint.feedback.value}"

    def send_bulk(self, ids: List[int]) -> None:

        url = f"{self._base_url}/{BackendEndpoints.bulk.value}"
        preamble = ("The following list of ids are from all the employees of the company."
                    "Used them to generate the feedback from and to. Try to give equal reviews positive and negative"
                    "Do not use other ids rather than the others provided"
                    f"List of ids: {ids}")
        data = DataSyntheticLLM(Feedback).create(num=30, preamble=preamble)
        response = requests.post(url, json=[d.model_dump() for d in data])
        if response.status_code == 200:
            print("Successfully sent data! Feedback")
            # Optional: Print the response from the server
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)
