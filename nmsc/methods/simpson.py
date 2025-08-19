"""
Module implementing Simpson's rule for numerical integration.

Functions
---------
_integral_over_one_interval_simpson : Computes the integral over a single interval
using Simpson's rule.
simpson : Computes the definite integral of a function over an interval using Simpson's
rule.
"""

import time
import numpy as np
from typing import Callable
from pydantic import validate_call
from nmsc._utils._validations import (
    _R_to_R_func_validator,
    _interval_bounds_validator,
    _interval_bounds_validator_simpson,
    _grid_pts_validator_simpson,
)
from nmsc._utils._helpers import MethodResults


def _integral_over_one_interval_simpson(
    f: Callable[[float], float], x_i: float, x_i_1: float, x_i_2: float
) -> float:

    x_i, x_i_1, x_i_2 = _interval_bounds_validator_simpson(x_i, x_i_1, x_i_2)
    h = x_i_2 - x_i
    integral = (h * (f(x_i) + 4 * f(x_i_1) + f(x_i_2))) / (6)
    return integral


@validate_call(validate_return=True)
def simpson(
    f: Callable[[float], float], a: float, b: float, grid_pts: int = 50
) -> MethodResults:
    """
    Compute the definite integral of a function over an interval using Simpson's rule.

    Parameters
    ----------
    f : Callable[[float], float]
        Function to integrate. Must accept and return a float.
    a : float
        Lower bound of the integration interval.
    b : float
        Upper bound of the integration interval.
    grid_pts : int, optional
        Number of grid points to use (default is 50, minimum is 3).

    Returns
    -------
    MethodResults
        Object containing the computed integral and the time taken (in seconds).

    Raises
    ------
    ValueError
        If input validation fails for function, interval bounds, or grid points.
    """
    f = _R_to_R_func_validator(func=f)
    a, b = _interval_bounds_validator(a, b)
    grid_pts = _grid_pts_validator_simpson(grid_pts=grid_pts, min_grid_pts=3)

    grid = np.linspace(a, b, grid_pts)
    integral = 0.0

    start_time = time.time()
    for i in range(0, grid_pts - 2, 2):
        integral += _integral_over_one_interval_simpson(
            f, grid[i], grid[i + 1], grid[i + 2]
        )
    end_time = time.time()
    req_time = round(end_time - start_time, 4)

    return MethodResults(integral, req_time)
