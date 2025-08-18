"""
Unit tests for nmsc.methods.midpoint
"""

import pytest
from nmsc.methods.midpoint import midpoint, _integral_over_one_interval_midpoint
from nmsc._utils._helpers import MethodResults


def test_integral_over_one_interval_midpoint():
    def f(x: float) -> float:
        return x

    # Integral of f(x) = x over [0, 1] using midpoint rule is 1 * f(0.5) = 0.5
    result = _integral_over_one_interval_midpoint(f, 0.0, 1.0)
    assert pytest.approx(result, 0.01) == 0.5
    # Should raise ValueError if bounds are wrong
    with pytest.raises(ValueError):
        _integral_over_one_interval_midpoint(f, 2.0, 1.0)


def test_midpoint_linear():
    def f(x: float) -> float:
        return x

    # Integral of f(x) = x over [0, 1] is 0.5
    result = midpoint(f, 0.0, 1.0, grid_pts=10)
    assert isinstance(result, MethodResults)
    assert pytest.approx(result.integral, 0.01) == 0.5


def test_midpoint_quadratic():
    def f(x: float) -> float:
        return x**2

    # Integral of x^2 over [0, 1] is 1/3
    result = midpoint(f, 0.0, 1.0, grid_pts=100)
    assert pytest.approx(result.integral, 0.01) == 1 / 3


def test_midpoint_invalid_func():
    def f(x: int) -> float:
        return float(x)

    with pytest.raises(TypeError):
        midpoint(f, 0.0, 1.0)


def test_midpoint_invalid_bounds():
    def f(x: float) -> float:
        return x

    with pytest.raises(ValueError):
        midpoint(f, 2.0, 1.0)


def test_midpoint_invalid_grid_pts():
    def f(x: float) -> float:
        return x

    with pytest.raises(ValueError):
        midpoint(f, 0.0, 1.0, grid_pts=1)
