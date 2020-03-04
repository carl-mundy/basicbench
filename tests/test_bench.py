import pytest

import basicbench

from . import utils


def test_can_create_new_bench_from_class():
    bench = utils.create_bench()
