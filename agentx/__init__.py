import logging

from agentx.agentx import AgentX
from agentx.version import VERSION

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %Z",
)

__all__ = ["AgentX"]
__version__ = VERSION
