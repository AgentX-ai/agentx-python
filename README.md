# AgentX Python SDK API library

[![PyPI version](https://img.shields.io/pypi/v/agentx-python)](https://pypi.org/project/agentx-python/)

The AgentX Python SDK provides a convenient way to access to your Agent programmatically.
This is a python SDK for AgentX (https://www.agentx.so/)

## Installation

```bash
pip install --upgrade agentx-python
```

## Usage

Provide an `api_key` inline or set `AGENTX_API_KEY` as an environment variable.
You can get an API key from https://app.agentx.so

### Agent

```python
from agentx_python import AgentX

client = AgentX(api_key="<your api key here>")

# Get the list of agents you have
print(client.list_agents())
```

### Conversation

Each Conversation has `agents` and `users` tied to it.

```python
# get agent
my_agent = client.get_agent(id="<agent id here>")

# Get the list of conversation from this agent
print(my_agent.list_conversations())
```

### Chat

A `chat` needs to happen in the conversation. You can do `stream` response too, default `False`.

```python
a_conversation = my_agent.get_conversation(id="<conversation id here>")

response = a_conversation.chat("Hello, what is your name?", stream=True)
for chunk in response:
    print(chunk, end="")

# output:
# My name is Rosita. I'm an AI assistant created by AgentX. It's nice to meet you! How can I help you today?
```
