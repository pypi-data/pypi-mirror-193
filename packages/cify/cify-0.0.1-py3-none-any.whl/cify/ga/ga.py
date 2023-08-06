import numpy as np

from cify import Algorithm, Position, ObjectiveFunction

from .crossover import uniform_crossover
from .mutate import mutate
from .select import top

__all__ = ["GA"]


class GA(Algorithm):
    def __init__(
        self,
        n: int,
        f: ObjectiveFunction,
        pm: float = 0.5,
        pc: float = 0.5,
        ms: float = 0.15,
    ):
        super().__init__()
        self.individuals = [Position(f) for _ in range(n)]
        self.pm = pm
        self.pc = pc
        self.ms = ms

    def iterate(self, f: ObjectiveFunction):
        n = len(self.individuals) // 2
        elite = top(n, self.individuals, f.opt)
        next_gen = []
        for parent_a in elite:
            parent_b_idx = int(np.random.uniform(0, len(elite) - 1))
            parent_b = elite[parent_b_idx]
            child_1, child_2 = uniform_crossover(parent_a, parent_b, self.pc)
            child_1 = mutate(child_1, self.pm, self.ms)
            child_2 = mutate(child_1, self.pm, self.ms)
            child_1(f)
            child_2(f)
            next_gen.append(child_1)
            next_gen.append(child_2)

        self.individuals = next_gen
