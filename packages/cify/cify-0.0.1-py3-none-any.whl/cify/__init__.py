import sys
from loguru import logger

from .algorithm import Algorithm
from .objective_function import ObjectiveFunction
from .optimization import Optimization
from .position import Position
from .random import rng, set_seed
from .task import Task
from .utils import positions

logger.remove()
logger.add(
    sys.stderr,
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> {level} <level>{message}</level>",
)


__all__ = [
    "Algorithm",
    "ObjectiveFunction",
    "Optimization",
    "Position",
    "Task",
    "rng",
    "set_seed",
    "positions",
]
