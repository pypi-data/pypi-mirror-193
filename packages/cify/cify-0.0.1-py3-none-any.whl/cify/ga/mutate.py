import numpy as np

from cify import Position, rng


__all__ = ["mutate"]


def mutate(individual: Position, pm, ms):
    mask = rng().uniform(size=individual.dim()) > pm
    mutations = rng().uniform(-ms, ms, size=individual.dim())
    individual += np.where(mask, mutations, 0.0)
    return individual
