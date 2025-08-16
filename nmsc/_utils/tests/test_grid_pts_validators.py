"""
Unit tests for nmsc._utils._validations._grid_pts_validators
"""

import pytest
from nmsc._utils._validations._grid_pts_validators import _grid_pts_validator


def test_valid_grid_pts():
    assert _grid_pts_validator(10, 2) == 10
    assert _grid_pts_validator(2, 2) == 2
    assert _grid_pts_validator(100, 2, 200) == 100


def test_too_few_grid_pts():
    with pytest.raises(ValueError):
        _grid_pts_validator(1, 2)
    with pytest.raises(ValueError):
        _grid_pts_validator(0, 2)


def test_too_many_grid_pts():
    with pytest.raises(ValueError):
        _grid_pts_validator(201, 2, 200)
    with pytest.raises(ValueError):
        _grid_pts_validator(200001, 2)
