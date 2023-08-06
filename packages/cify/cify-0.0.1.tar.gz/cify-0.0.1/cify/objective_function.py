from typing import Callable, List, Union
import numpy as np
from .random import rng
from .optimization import Optimization

__all__ = ["ObjectiveFunction"]


class ObjectiveFunction(object):
    """Defines an objective function to be optimized."""

    def __init__(
        self,
        f: Callable,
        bounds: list,
        dim: int = None,
        opt: Optimization = Optimization.Min,
        name: str = "",
    ):
        """
        :param f: The function to be optimized.
        :param bounds: The bounds of the search space. Bounds should be passed
        in as a list of lists, e.g. [[L, U], [L, U]], or as a [L, U] and use
        the dim parameter to specify the dimensions.
        :param dim: The number of dimensions. If unspecified, the length of the
        bounds will be used.
        :param optimization: Indicates whether the :class:`ObjectiveFunction`
        is to be minimized or maximized.
        :param name: An optional name for the objective function. If
        unspecified, the function name will be used.
        """
        self.__f = None
        self.__bounds = None
        self.__dim = dim
        self.__opt = opt
        self.__evaluations = 0
        self.__value = opt.default()

        self.f = f
        self.bounds = bounds

        if f.__name__ == "<lambda>" and name == "":
            name = "lambda"

        self.name = name if name else self.f.__name__

    @property
    def f(self) -> Callable:
        """Returns the function to be optimized."""
        return self.__f

    @property
    def opt(self) -> Optimization:
        """
        Returns the :class:`ObjectiveFunction`'s optimization type, either
        minimization or maximization.
        """
        return self.__opt

    @property
    def bounds(self) -> list:
        """
        The boundary constraints represented as a list of the form:

        `[[LB1, UB1], ..., [LBn, UBn]]`

        where UB is the upper bound and LB is the lower bound of the search
        space for that dimension. Can also be passed as a list of the form:

        `[LB, UB]`

        where the bounds will apply to all dimensions of the search space.
        """
        return self.__bounds

    @property
    def evaluations(self) -> int:
        """
        Returns the number of evaluations performed and resets the counter.

        :return: Number of function evaluations.
        """
        return self.__evaluations

    @f.setter
    def f(self, function):
        """Sets the function to be optimized."""
        if not isinstance(function, Callable):
            raise TypeError(
                f"function: Expected callable, received" f"{type(function)}"
            )

        self.__f = function

    @opt.setter
    def opt(self, opt):
        """Sets the :class:`Optimization` type."""
        if not isinstance(opt, Optimization):
            raise TypeError(f"function: Expected callable, received" f"{type(opt)}")

        self.__opt = opt

    @bounds.setter
    def bounds(self, bounds):
        """Sets the boundary constraints of the search space."""
        if not isinstance(bounds, list):
            raise Exception("oh no")

        dim = self.__dim

        if len(bounds) == 0:
            raise Exception("Oh no")
        if isinstance(bounds[0], list):
            self.__bounds = bounds
            return

        if len(bounds) == 2:
            bounds = [bounds] * dim

        self.__bounds = bounds

    def cmp(self, a, b) -> bool:
        """
        Returns whether ``a`` is better than ``b``.
        """
        return self.opt.cmp(a, b)

    def dim(self) -> int:
        """The number of dimensions of the search space."""
        return len(self.__bounds)

    def eval(self, vector) -> float:
        """
        Evaluates a vector using the objective function.

        :param vector: The vector to evaluate.
        """
        self.__evaluations += 1
        self.value = self.f(vector)
        return self.value

    def in_bounds(self, vector: Union[np.ndarray, List], index: int = None):
        """
        Returns whether the vector is within the bounds of the optimization
        problem.
        """
        if index:
            lower, upper = self.bounds[index]
            return lower <= vector[index] <= upper

        for i, (lower, upper) in enumerate(self.bounds):
            if vector[i] < lower or vector[i] > upper:
                return False

        return True

    def lower_bounds(self) -> list:
        """
        Returns a list of floats consisting of the lower bounds of the
        :class:`ObjectiveFunction` search space per dimension.
        """
        return [i[0] for i in self.__bounds]

    def upper_bounds(self) -> list:
        """
        Returns a list of floats consisting of the upper bounds of the
        :class:`ObjectiveFunction` search space per dimension.
        """
        return [i[1] for i in self.__bounds]

    def sample(self) -> np.ndarray:
        """
        Uniformly samples a vector from the bounds of the optimization problem.
        """
        position = []
        for i in range(len(self.bounds)):
            lower, upper = self.bounds[i]
            position.append(rng().uniform(lower, upper))

        return np.array(position)

    def __call__(self, vector):
        return self.eval(vector)

    def __str__(self) -> str:
        """Returns a str representation of the :class:`ObjectiveFunction`"""
        return f"{self.opt.verb()}: {self.name}\nBounds: {self.bounds}"
