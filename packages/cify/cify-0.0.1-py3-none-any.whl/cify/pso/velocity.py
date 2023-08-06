from cify.position import Position
from cify.pso.particle import Particle
from cify.random import rng


__all__ = ["std_velocity"]


def std_velocity(
    particle: Particle,
    social_best: Position,
    w: float = 0.74,
    c1: float = 1.4,
    c2: float = 1.4,
):
    """
    The default velocity update function.

    :param particle: The particle whose velocity is to be updated.
    :param social_best: The social guide.
    :param w: Inertia weight.
    :param c1: Cognitive acceleration coefficient.
    :param c2: Social acceleration coefficient.
    """
    r1 = rng().uniform(0.0, 1.0, particle.position.dim())
    r2 = rng().uniform(0.0, 1.0, particle.position.dim())
    return (
        (w * particle.velocity)
        + (r1 * c1 * (particle.personal_best - particle.position))
        + (r2 * c2 * (social_best - particle.position))
    )
