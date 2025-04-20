from typing import List
import requests
import os
import logging

from agentx.util import get_headers
from agentx.resources.agent import Agent


class AgentX:

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("AGENTX_API_KEY")
        if self.api_key and not os.getenv("AGENTX_API_KEY"):
            os.environ["AGENTX_API_KEY"] = self.api_key

    def get_agent(self, id: str) -> Agent:
        url = f"https://api.agentx.so/api/v1/access/agents/{id}"
        # Make a GET request to the AgentX API
        response = requests.get(url, headers=get_headers())
        # Check if response was successful
        if response.status_code == 200:
            agent_res = response.json()
            return Agent(
                id=agent_res.get("_id"),
                name=agent_res.get("name"),
                avatar=agent_res.get("avatar"),
                createdAt=agent_res.get("createdAt"),
                updatedAt=agent_res.get("updatedAt"),
            )
        else:
            raise Exception(f"Failed to retrieve agent: {response.reason}")

    def list_agents(self) -> List[Agent]:
        url = "https://api.agentx.so/api/v1/access/agents"
        # Make a GET request to the AgentX API
        response = requests.get(url, headers=get_headers())
        # Check if response was successful
        if response.status_code == 200:
            return [
                Agent(
                    id=agent_res.get("_id"),
                    name=agent_res.get("name"),
                    avatar=agent_res.get("avatar"),
                    createdAt=agent_res.get("createdAt"),
                    updatedAt=agent_res.get("updatedAt"),
                )
                for agent_res in response.json()
            ]
        else:
            raise Exception(f"Failed to list agents: {response.reason}")
