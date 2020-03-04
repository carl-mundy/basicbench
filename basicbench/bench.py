from typing import List

from .experiment import Experiment


class Bench:

    def __init__(self):
        self._experiments = []

    def new(self, *args, **kwargs) -> Experiment:
        """Return a new Experiment for usage"""
        return Experiment(*args, **kwargs)

    def list(self) -> List[Experiment]:
        return self._experiments

