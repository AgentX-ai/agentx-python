import logging
import os

from agentx_python.agent import Agent
from agentx_python.version import VERSION

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %Z",
)


api_key = os.environ.get("OPENAI_API_KEY")

Agent = Agent()

__version__ = VERSION
__all__ = ["api_key", "Agent"]
