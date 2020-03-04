from .experiment import Experiment


class Bench:

    def new(self, *args, **kwargs) -> Experiment:
        """Return a new Experiment for usage"""
        return Experiment(*args, **kwargs)
