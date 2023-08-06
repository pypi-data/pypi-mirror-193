from cify.objective_function import ObjectiveFunction
from cify.position import Position


__all__ = ["positions"]


def positions(n: int, f: ObjectiveFunction):
    """
    :return: A list of n positions.
    """
    return [Position(f=f) for _ in range(n)]
