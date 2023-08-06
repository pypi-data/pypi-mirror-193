import numpy as np

from cify import logger

__all__ = ["rng", "set_seed"]

__seed = None
__rng = np.random.default_rng(__seed)


def rng() -> np.random.Generator:
    """
    Returns the global random number generator used for stochastic operations.
    """
    global __rng
    return __rng


def set_seed(seed):
    """
    Sets the global seed for the internal random number generator.

    :param seed: The seed value to be used by the generator, defaults to None
    :type seed: None, int, array-like[ints], numpy.SeedSequence, BitGenerator,
    Generator, optional
    """
    global __rng, __seed
    try:
        __seed = seed
        __rng = np.random.default_rng(__seed)
        logger.info("CIFY: internal seed successfully set to: '%s'" % seed)
    except Exception:
        logger.error("CIFY: internal seed could not be set!")
