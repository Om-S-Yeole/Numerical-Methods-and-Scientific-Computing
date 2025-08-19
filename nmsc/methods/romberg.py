"""
Module implementing Romberg integration for numerical integration.

Functions
---------
_dynamic_h_calculator : Calculates the step size h for Romberg integration.
_R_n_m : Computes the Romberg table entry R(n, m).
romberg : Computes the definite integral of a function over an interval using Romberg
integration.
"""

import time
from typing import Callable
from pydantic import validate_call
from nmsc._utils._validations import (
    _R_to_R_func_validator,
    _interval_bounds_validator,
    _romberg_hyperparameters_validator,
)
from nmsc._utils._helpers import MethodResults


def _dynamic_h_calculator(a: float, b: float, n: int) -> float:
    return (b - a) / (2 ** (n + 1))


def _R_n_m(f: Callable[[float], float], a: float, b: float, n: int, m: int) -> float:
    """
    Compute the Romberg table entry R(n, m).

    Parameters
    ----------
    f : Callable[[float], float]
        Function to integrate.
    a : float
        Lower bound of the interval.
    b : float
        Upper bound of the interval.
    n : int
        Row index in Romberg table (refinement level).
    m : int
        Column index in Romberg table (extrapolation level).

    Returns
    -------
    float
        Value of R(n, m) in the Romberg table.

    Raises
    ------
    ValueError
        If n or m are invalid according to _romberg_hyperparameters_validator.
    """
    n, m = _romberg_hyperparameters_validator(n, m)
    if (n == 0) and (m == 0):
        h_0 = _dynamic_h_calculator(a, b, n)
        r_0_0 = h_0 * (f(a) + f(b))
        return r_0_0
    elif (n != 0) and (m == 0):
        h_n = _dynamic_h_calculator(a, b, n)
        f_sum = 0.0
        for k in range(1, 2 ** (n - 1) + 1):
            f_sum += f(a + (2 * k - 1) * _dynamic_h_calculator(a, b, n - 1))
        r_n_0 = (_R_n_m(f, a, b, n - 1, 0)) / (2) + 2 * h_n * f_sum
        return r_n_0
    else:
        r_n_m = (
            (4**m) * _R_n_m(f, a, b, n, m - 1) - _R_n_m(f, a, b, n - 1, m - 1)
        ) / (4**m - 1)
        return r_n_m


@validate_call(validate_return=True)
def romberg(
    f: Callable[[float], float], a: float, b: float, n: int, m: int
) -> MethodResults:
    """
    Compute the definite integral of a function over an interval using Romberg
    integration.

    Parameters
    ----------
    f : Callable[[float], float]
        Function to integrate. Must accept and return a float.
    a : float
        Lower bound of the integration interval.
    b : float
        Upper bound of the integration interval.
    n : int
        Row index in Romberg table (refinement level).
    m : int
        Column index in Romberg table (extrapolation level).

    Returns
    -------
    MethodResults
        Object containing the computed integral and the time taken (in seconds).

    Raises
    ------
    ValueError
        If input validation fails for function, interval bounds, or hyperparameters.
    """
    a, b = _interval_bounds_validator(a, b)
    f = _R_to_R_func_validator(f)
    start_time = time.time()
    integral = _R_n_m(f, a, b, n, m)
    end_time = time.time()
    req_time = round(end_time - start_time, 4)
    return MethodResults(integral, req_time)
