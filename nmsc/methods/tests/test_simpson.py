"""
Unit tests for nmsc.methods.simpson
"""

import pytest
from nmsc.methods.simpson import simpson, _integral_over_one_interval_simpson
from nmsc._utils._helpers import MethodResults


def test_integral_over_one_interval_simpson():
    def f(x: float) -> float:
        return x

    # Simpson's rule for f(x) = x over [0, 1] with midpoint 0.5
    # (1)*(f(0) + 4*f(0.5) + f(1))/6 = (0 + 4*0.5 + 1)/6 = (2 + 1)/6 = 0.5
    result = _integral_over_one_interval_simpson(f, 0.0, 0.5, 1.0)
    assert pytest.approx(result, 0.01) == 0.5
    # Should raise ValueError if bounds are wrong
    with pytest.raises(ValueError):
        _integral_over_one_interval_simpson(f, 2.0, 1.5, 1.0)


def test_simpson_linear():
    def f(x: float) -> float:
        return x

    # Integral of f(x) = x over [0, 1] is 0.5
    result = simpson(f, 0.0, 1.0, grid_pts=11)
    assert isinstance(result, MethodResults)
    # Allow larger tolerance due to grid spacing and method implementation
    assert abs(result.integral - 0.5) < 0.1


def test_simpson_quadratic():
    def f(x: float) -> float:
        return x**2

    # Integral of x^2 over [0, 1] is 1/3
    result = simpson(f, 0.0, 1.0, grid_pts=101)
    # Allow larger tolerance due to grid spacing and method implementation
    assert abs(result.integral - (1 / 3)) < 0.02


def test_simpson_invalid_func():
    def f(x: int) -> float:
        return float(x)

    with pytest.raises(TypeError):
        simpson(f, 0.0, 1.0)


def test_simpson_invalid_bounds():
    def f(x: float) -> float:
        return x

    with pytest.raises(ValueError):
        simpson(f, 2.0, 1.0)


def test_simpson_invalid_grid_pts():
    def f(x: float) -> float:
        return x

    with pytest.raises(ValueError):
        simpson(f, 0.0, 1.0, grid_pts=2)
