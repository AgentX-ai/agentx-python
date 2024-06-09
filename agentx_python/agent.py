import requests
import os
import logging
import agentx_python as agentx
from functools import wraps


def api_key_check_decorator(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self.middleware()
        return method(self, *args, **kwargs)

    return wrapper


class Agent:

    def middleware(self):
        self.api_key = os.getenv("AGENTX_API_KEY") or agentx.api_key
        if not self.api_key:
            raise Exception(
                "No API key provided. You can set your API key in code using 'agentx.api_key = <API-KEY>', or you can set the environment variable AGENTX_API_KEY=<API-KEY>). You can generate API keys in the AgentX https://app.agentx.so."
            )

    @api_key_check_decorator
    def get_agent(self, id: str):
        url = f"https://api.agentx.so/api/v1/access/agents/{id}"
        headers = {"accept": "*/*", "x-api-key": self.api_key}

        # Make a GET request to the AgentX API
        response = requests.get(url, headers=headers)
        # Check if response was successful
        if response.status_code == 200:
            return response.json()
        else:
            logging.info(
                response.json()
            )  # Print text content of response (or process it as needed)
            raise Exception(
                f"Failed to retrieve agent details: {response.status_code} - {response.reason}"
            )

    @api_key_check_decorator
    def list_agents(self):
        url = "https://api.agentx.so/api/v1/access/agents"
        headers = {"accept": "*/*", "x-api-key": self.api_key}

        # Make a GET request to the AgentX API
        response = requests.get(url, headers=headers)
        # Check if response was successful
        if response.status_code == 200:
            return response.json()
        else:
            logging.info(response.json())
