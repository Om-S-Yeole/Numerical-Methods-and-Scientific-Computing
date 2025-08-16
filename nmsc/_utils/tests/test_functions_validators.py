"""
Unit tests for nmsc._utils._validations._functions_validators
"""

import pytest
from nmsc._utils._validations._functions_validators import _R_to_R_func_validator


def test_valid_func():
    def f(x: float) -> float:
        return x * 2

    assert _R_to_R_func_validator(f) is f


def test_invalid_num_args():
    def f(x: float, y: float) -> float:
        return x + y

    with pytest.raises(ValueError):
        _R_to_R_func_validator(f)


def test_invalid_arg_type():
    def f(x: int) -> float:
        return float(x)

    with pytest.raises(TypeError):
        _R_to_R_func_validator(f)


def test_invalid_return_type():
    def f(x: float) -> int:
        return int(x)

    with pytest.raises(TypeError):
        _R_to_R_func_validator(f)
