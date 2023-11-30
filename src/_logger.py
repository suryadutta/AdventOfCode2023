import logging
import os
import sys

LOGGER = logging.getLogger("canary_python")
logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)
LOGGER.setLevel(int(os.getenv("LOGGING_LEVEL", str(logging.INFO))))

__all__ = ["LOGGER"]
