import numpy as np

from cify import Position, rng


__all__ = ["uniform_crossover"]


def uniform_crossover(parent_a: Position, parent_b: Position, pc):
    mask = rng().uniform(size=parent_a.dim()) > pc
    child_1 = np.where(mask, parent_b.vector, parent_b.vector)
    child_2 = np.where(~mask, parent_b.vector, parent_b.vector)
    return Position(child_1), Position(child_2)
