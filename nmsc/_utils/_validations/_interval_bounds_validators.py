"""
Module for validating interval bounds.

Functions:
    _interval_bounds_validator: Validates that the lower bound is less than the upper
    bound.
"""

from pydantic import validate_call


@validate_call(validate_return=True)
def _interval_bounds_validator(a: float, b: float) -> tuple[float, float]:

    if a > b:
        raise ValueError(
            f"Lower bound 'a' must be less than upper bound 'b'. Got a={a}, b={b}"
        )

    return (a, b)
