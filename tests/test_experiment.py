import pytest

import basicbench

from . import utils


def test_can_make_new_named_experiment_from_bench():
    experiment = utils.create_experiment('my-experiment')


def test_new_named_experiment_has_name():
    experiment = utils.create_experiment('my-experiment')
    assert experiment.name == 'my-experiment'

def test_new_named_experiment_has_id():
    experiment = utils.create_experiment('my-experiment')
    assert experiment.id

def test_new_named_experiment_has_created date():
    experiment = utils.create_experiment('my-experiment')
    assert experiment.created 
