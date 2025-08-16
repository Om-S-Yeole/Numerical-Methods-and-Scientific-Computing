"""
Unit tests for nmsc.methods.trapezoidal
"""

import pytest
from nmsc.methods.trapezoidal import trapezoidal, _integral_over_one_interval_trap


def test_integral_over_one_interval_trap():
    def f(x: float) -> float:
        return x

    # Integral of f(x) = x over [0, 1] is 0.5
    result = _integral_over_one_interval_trap(f, 0.0, 1.0)
    assert pytest.approx(result, 0.01) == 0.5
    # Should raise ValueError if bounds are wrong
    with pytest.raises(ValueError):
        _integral_over_one_interval_trap(f, 2.0, 1.0)


def test_trapezoidal_linear():
    def f(x: float) -> float:
        return x

    # Integral of f(x) = x over [0, 1] is 0.5
    result, _ = trapezoidal(f, 0.0, 1.0, grid_pts=10)
    assert pytest.approx(result, 0.01) == 0.5


def test_trapezoidal_quadratic():
    def f(x: float) -> float:
        return x**2

    # Integral of x^2 over [0, 1] is 1/3
    result, _ = trapezoidal(f, 0.0, 1.0, grid_pts=100)
    assert pytest.approx(result, 0.01) == 1 / 3


def test_trapezoidal_invalid_func():
    def f(x: int) -> float:
        return float(x)

    with pytest.raises(TypeError):
        trapezoidal(f, 0.0, 1.0)


def test_trapezoidal_invalid_bounds():
    def f(x: float) -> float:
        return x

    with pytest.raises(ValueError):
        trapezoidal(f, 2.0, 1.0)


def test_trapezoidal_invalid_grid_pts():
    def f(x: float) -> float:
        return x

    with pytest.raises(ValueError):
        trapezoidal(f, 0.0, 1.0, grid_pts=1)
