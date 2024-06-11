import logging

from agentx_python.agentx import AgentX
from agentx_python.version import VERSION

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %Z",
)

__all__ = ["AgentX"]
__version__ = VERSION
