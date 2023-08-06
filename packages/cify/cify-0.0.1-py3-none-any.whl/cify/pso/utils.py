from typing import List

from cify.objective_function import ObjectiveFunction
from cify.pso.particle import Particle


__all__ = ["particles", "global_best"]


def particles(n: int, f: ObjectiveFunction):
    return [Particle(f=f) for _ in range(n)]


def global_best(particles: List[Particle], f: ObjectiveFunction):
    best = particles[0].personal_best
    for particle in particles[1:]:
        best = f.opt.best(best, particle.personal_best)
    return best
