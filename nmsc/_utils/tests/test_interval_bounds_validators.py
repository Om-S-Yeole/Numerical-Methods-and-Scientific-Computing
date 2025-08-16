"""
Unit tests for nmsc._utils._validations._interval_bounds_validators
"""

import pytest
from nmsc._utils._validations._interval_bounds_validators import (
    _interval_bounds_validator,
)


def test_valid_bounds():
    assert _interval_bounds_validator(1.0, 2.0) == (1.0, 2.0)
    assert _interval_bounds_validator(-5.0, 0.0) == (-5.0, 0.0)


def test_invalid_bounds():
    with pytest.raises(ValueError):
        _interval_bounds_validator(2.0, 1.0)
    with pytest.raises(ValueError):
        _interval_bounds_validator(0.0, -1.0)
