from typing import List

from .experiment import Experiment


class Bench:

    def __init__(self):
        self._experiments = []

    def new(self, *args, **kwargs) -> Experiment:
        """Return a new Experiment for usage"""
        experiment = Experiment(*args, **kwargs)
        self._experiments.append(experiment)
        return experiment

    def list(self) -> List[Experiment]:
        return self._experiments

