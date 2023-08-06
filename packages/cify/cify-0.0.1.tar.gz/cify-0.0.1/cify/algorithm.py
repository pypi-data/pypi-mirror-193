from abc import ABC, abstractmethod

from .objective_function import ObjectiveFunction

__all__ = ["Algorithm"]


class Algorithm(ABC):
    """Minimal base class for CIFY algorithms. The only required method to
    implement is the ``iterate`` method which is used in :class:`Task`.

    """

    def __init__(self, name: str = ""):
        """
        :param name: An optional name for the :class:`Algorithm`. If name isn't
            specified, the class name will be used.
        """
        self.name = name if name else self.__class__.__name__

    @abstractmethod
    def iterate(self, f: ObjectiveFunction):
        """
        The only function that must be overridden when implementing your own
        algorithm. This function must be the logic of one iteration of your
        algorithm.

        :param f: The :class:`ObjectiveFunction` to optimize.
        """
        pass

    def __str__(self) -> str:
        return self.name
