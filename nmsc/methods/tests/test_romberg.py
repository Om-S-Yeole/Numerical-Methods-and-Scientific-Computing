"""
Unit tests for nmsc.methods.romberg
"""

import pytest
from nmsc.methods.romberg import romberg, _R_n_m, _dynamic_h_calculator
from nmsc._utils._helpers import MethodResults


def test_dynamic_h_calculator():
    h = _dynamic_h_calculator(0.0, 1.0, 0)
    assert h == 0.5
    h2 = _dynamic_h_calculator(0.0, 1.0, 1)
    assert h2 == 0.25


def test_R_n_m_base_case():
    def f(x: float) -> float:
        return x

    # R(0,0) for f(x)=x over [0,1] should be 0.5*(f(0)+f(1)) = 0.5
    result = _R_n_m(f, 0.0, 1.0, 0, 0)
    assert pytest.approx(result, 0.01) == 0.5


def test_romberg_linear():
    def f(x: float) -> float:
        return x

    # Integral of f(x)=x over [0,1] is 0.5
    result = romberg(f, 0.0, 1.0, n=4, m=4)
    assert isinstance(result, MethodResults)
    assert abs(result.integral - 0.5) < 0.01


def test_romberg_quadratic():
    def f(x: float) -> float:
        return x**2

    # Integral of x^2 over [0,1] is 1/3
    result = romberg(f, 0.0, 1.0, n=4, m=4)
    assert abs(result.integral - (1 / 3)) < 0.01


def test_romberg_invalid_func():
    def f(x: int) -> float:
        return float(x)

    with pytest.raises(TypeError):
        romberg(f, 0.0, 1.0, n=2, m=2)


def test_romberg_invalid_bounds():
    def f(x: float) -> float:
        return x

    with pytest.raises(ValueError):
        romberg(f, 2.0, 1.0, n=2, m=2)


def test_romberg_invalid_hyperparameters():
    def f(x: float) -> float:
        return x

    with pytest.raises(ValueError):
        romberg(f, 0.0, 1.0, n=-1, m=2)
    with pytest.raises(ValueError):
        romberg(f, 0.0, 1.0, n=2, m=-1)
