from typing import Optional, List
from pydantic import BaseModel, Field
import os
import requests
from agentx_python.util import get_headers


class Conversation(BaseModel):
    agent_id: str
    id: str
    title: Optional[str] = Field(default=None)  # conversation customized title
    users: List[str]
    agents: List[str]
    createdAt: Optional[str]
    updatedAt: Optional[str]

    def __init__(self, **data):
        super().__init__(**data)

    def generate_conversation_id(self):
        return "generate new_conversation_id"

    def list_messages(self):
        url = f"https://api.agentx.so/api/v1/access/agents/{self.agent_id}/conversations/{self.id}"
        response = requests.get(url, headers=get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Failed to retrieve agent details: {response.status_code} - {response.reason}"
            )

    def chat(self, message: str, stream: bool = False, context: int = None):
        if stream:
            return self._chat_stream(message, context)
        else:
            url = f"https://api.agentx.so/api/v1/access/conversations/{self.id}/message"
            response = requests.post(
                url,
                headers=get_headers(),
                json={"message": message, "context": context},
            )
            return response.json()

    def _chat_stream(self, message: str, context: int = None):
        url = f"https://api.agentx.so/api/v1/access/conversations/{self.id}/messagesse"
        response = requests.post(
            url, headers=get_headers(), json={"message": message, "context": context}
        )
        if response.status_code == 200:
            buf = b""
            for chunk in response.iter_content():
                buf += chunk
                try:
                    chunk = buf.decode("utf-8")
                    yield chunk
                except UnicodeDecodeError:
                    continue
                buf = b""
        else:
            raise Exception(
                f"Failed to send message: {response.status_code} - {response.reason}"
            )
