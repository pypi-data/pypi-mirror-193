from cify.algorithm import Algorithm
from cify.pso.utils import global_best, particles
from cify.pso.velocity import std_velocity


__all__ = ["PSO"]


class PSO(Algorithm):
    def __init__(self, n_particles: int, obj_func, w: float, c1: float, c2: float):
        """
        :param n_particles: The number of particles in the Swarm.
        :param obj_func: The :class:`ObjectiveFunction` used to initialize the
            particles.
        :param w: Inertia weight.
        :param c1: Cognitive acceleration coefficient.
        :param c2: Social acceleration coefficient.
        """
        super().__init__()
        self.particles = particles(n_particles, obj_func)
        self.w = w
        self.c1 = c1
        self.c2 = c2

    def iterate(self, obj_func) -> None:
        gb = global_best(self.particles, obj_func)
        for particle in self.particles:
            velocity = std_velocity(particle, gb)
            particle.velocity = velocity
            particle.position = (particle.position + velocity).vector
            particle.evaluate(obj_func)
            particle.update_personal_best()

    def collection(self):
        return self.particles
