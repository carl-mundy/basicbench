import pytest

import basicbench

from . import utils


def test_can_create_new_bench_from_class():
    bench = utils.create_bench()
    assert bench

def test_bench_remembers_experiments():
    bench = utils.create_bench()

    assert bench.list() == []

def test_bench_remembers_new_experiment():
    bench = utils.create_bench()
    experiment = bench.new('test')

    assert len(bench.list()) == 1
