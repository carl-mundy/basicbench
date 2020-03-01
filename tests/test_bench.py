import pytest

import basicbench


def test_can_create_new_bench_from_class():
    bench = basicbench.Bench()


@pytest.fixture
def bench():
    return basicbench.Bench()


def test_can_make_new_experiment_from_bench(bench):
    experiment = bench.new()
