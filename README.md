![Logo](https://agentx-resources.s3.us-west-1.amazonaws.com/AgentX-logo-387x60.png)

[![PyPI version](https://img.shields.io/pypi/v/agentx-python)](https://pypi.org/project/agentx-python/)

---

## a fast way to build AI Agents and create agent workforce

The official AgentX Python SDK for [AgentX](https://www.agentx.so/)

Why build AI agent with AgentX?

- Simplicity, Agent - Conversation - Message structure.
- Include chain-of-thoughts.
- Choose from most open and closed sourced LLM vendors.
- Built-in Voice(ASR, TTS), Image Gen, Document, CSV/excel tool, OCR, etc.
- Support all running MCP (model context protocol).
- Support RAG with built-in re-rank.
- Multi-agent workforce orchestration.
- Multiple agents working together with a designated manager agent.
- Cross LLM vendor, multi-agent orchestration.
- A2A - agent to agent protocol

## Installation

```bash
pip install --upgrade agentx-python
```

## Quick Start

Get started with AgentX in just a few lines of code:

```python
from agentx import AgentX

# Initialize the client
client = AgentX(api_key="your-api-key-here")

# Get your agents
agents = client.list_agents()
print(f"You have {len(agents)} agents")

# Start chatting with your first agent
if agents:
    agent = agents[0]
    conversation = agent.new_conversation()
    response = conversation.chat("Hello! What can you help me with?")
    print(response)
```

## Usage

Provide an `api_key` inline or set `AGENTX_API_KEY` as an environment variable.
You can get an API key from https://app.agentx.so

### Agent

```python
from agentx import AgentX

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
existing_conversations = my_agent.list_conversations()
print(existing_conversations)

# Get the list of history messages from a conversation
last_conversation = existing_conversations[-1]
msgs = last_conversation.list_messages()
print(msgs)
```

### Chat

A `chat` needs to happen in the conversation. You can do `stream` response too, default `False`.

```python
a_conversation = my_agent.get_conversation(id="<conversation id here>")

response = a_conversation.chat_stream("Hello, what is your name?")
for chunk in response:
    print(chunk)
```

output looks like:

```
text=None cot='The user is greeting and asking for my ' botId='xxx'
text=None cot='name, which are casual, straightforward questions.' botId='xxx'
text=None cot=' I can answer these directly' botId='xxx'
text='Hello' cot=None botId='xxx'
text='!' cot=None botId='xxx'
text=' I' cot=None botId='xxx'
text=' am' cot=None botId='xxx'
text=' AgentX' cot=None botId='xxx'
text=None cot=None botId='xxx'
```

\*`cot` stands for chain-of-thoughts

### Workforce

A Workforce (team) consists of multiple agents working together with a designated manager agent.

```python
from agentx import AgentX

client = AgentX(api_key="<your api key here>")

# Get the list of workforces/teams you have
workforces = client.list_workforces()
print(workforces)

# Get a specific workforce
workforce = workforces[0]  # or any specific workforce
print(f"Workforce: {workforce.name}")
print(f"Manager: {workforce.manager.name}")
print(f"Agents: {[agent.name for agent in workforce.agents]}")
```

#### Workforce Conversations

```python
# Create a new conversation with the workforce
conversation = workforce.new_conversation()

# List all existing conversations for the workforce
conversations = workforce.list_conversations()
print(conversations)
```

#### Chat with Workforce

Chat with the entire workforce team and get streaming responses from all agents.

```python
# Stream chat with the workforce
response = workforce.chat_stream(conversation.id, "How can you help me with this project?")
for chunk in response:
    if chunk.text:
        print(chunk.text, end="")
    if chunk.cot:
        print(f" [COT: {chunk.cot}]")
```

The workforce chat allows you to leverage multiple specialized agents working together to provide comprehensive responses to your queries.
