from operator import floordiv
import time

import numpy as np

from .optimization import Optimization
from loguru import logger

__all__ = ["Task"]


class Task(object):
    """
    Defines a task to be executed.
    """

    def __init__(
        self,
        optimizer,
        f,
        optimization=Optimization.Min,
        max_evaluations=np.inf,
        max_iterations=np.inf,
        cutoff_value=None,
        log_evaluations=None,
        log_iterations=None,
        metrics=None,
    ):
        self.value = None
        self.f = f
        self.opt = optimization
        self.iterations = 0
        self.max_iterations = max_iterations
        self.max_evaluations = max_evaluations
        self.cutoff_value = cutoff_value
        self.log_evaluations = log_evaluations
        self.log_iterations = log_iterations
        self.optimizer = optimizer
        self.start_time = None
        self.end_time = None
        self.metrics = metrics
        self.results = {}
        if metrics:
            for name, _ in metrics:
                self.results[name] = []

    def eval(self, vector) -> float:
        """
        :return: The objective function value of the vector.
        """
        if self.stopping_condition():
            return self.opt.default()

        self.value = self.f(vector)

        if self.log_evaluations and self.f.evaluations % self.log_evaluations == 0:
            self.log()

        return self.value

    def stopping_condition(self) -> bool:
        """
        :return: Whether the stopping condition has been reached.
        """
        if self.f.evaluations >= self.max_evaluations:
            return True

        if self.iterations >= self.max_iterations:
            return True

        if self.cutoff_value:
            return self.f.opt.cmp(self.value, self.cutoff_value, equal=True)

        return False

    def next_iteration(self):
        """
        Increments the iterations counter.
        """
        self.iterations += 1

        if self.log_iterations and self.iterations % self.log_iterations == 0:
            self.log()

    def run(self):
        """
        Optimizes the objective function.
        """
        self.start()
        while not self.stopping_condition():
            self.optimizer.iterate(self.f)
            if self.metrics:
                for name, metric in self.metrics:
                    self.results[name].append(metric(self.optimizer, self.f))
            self.next_iteration()
        self.end()

    def start(self):
        """
        Start recording the time taken to optimize.
        """
        self.start_time = time.time()

    def end(self):
        """
        End recording the time taken to optimize.
        """
        self.start_time = time.time()

    def time_taken(self) -> float:
        """
        :return: Time taken in seconds to optimize..
        """
        if self.start_time is None:
            return 0.0

        if self.end_time is None:
            return time.time() - self.start_time

        return self.end_time - self.start_time

    def log(self, verbose=True):
        optimization = self.opt.verb()
        f = self.f.name
        progress = self.__progress_string()
        value = f"{self.f.value:.3f}"

        message = f"<blue>{self.optimizer}</blue> "
        message += f"{optimization} "
        message += f"{f} "
        message += f"[<yellow>{progress}</yellow>]"
        message += f": {value}"

        if verbose:
            iterations = f"Iterations: {self.iterations}"
            if self.max_iterations != np.inf:
                iterations += f"/{self.max_iterations}"

            evaluations = f"Evaluations: {self.f.evaluations}"
            if self.max_evaluations != np.inf:
                evaluations += f"/{self.max_evaluations}"

            time_taken = f"Time Taken: {self.__time_taken_string()}"
            eta = f"ETA: {self.__eta_string()}"

            message += f" -- {iterations}, "
            message += f"{evaluations}, "
            message += f"{time_taken}, "
            message += f"{eta}"

        logger.opt(ansi=True).info(message)

    def __time_taken_string(self):
        time_taken = self.time_taken()
        if time_taken is None:
            return "Not started"

        return f"{time_taken:.3f}s"

    def __eta(self):
        time_taken = self.time_taken()
        if time_taken is None:
            return None

        progress = self.__progress()
        if progress is None:
            return None

        return (time_taken / progress) - time_taken

    def __eta_string(self):
        eta = self.__eta()
        if eta is None:
            return "Not started"

        return f"{eta:.3f}s"

    def __progress(self):
        progress = 0.0
        if self.max_iterations != np.inf:
            progress = self.iterations / self.max_iterations

        if self.max_evaluations != np.inf:
            if progress == 0.0:
                progress = self.f.evaluations / self.max_evaluations
            else:
                progress += self.f.evaluations / self.max_evaluations
                progress /= 2

        return progress

    def __progress_string(self):
        return f"{(self.__progress() * 100):.2f}%"
