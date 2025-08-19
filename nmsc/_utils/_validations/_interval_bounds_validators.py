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
    if b - a > 100000:
        raise ValueError(
            "Difference between the upper and lower bound is restricted to be less "
            "than 100000 in order to avoid memory overflow and potential abuse of api. "
            f"Got a={a}, b={b} and difference={b-a}"
        )

    return (a, b)


@validate_call(validate_return=True)
def _interval_bounds_validator_simpson(
    x_i: float, x_i_1: float, x_i_2: float
) -> tuple[float, float, float]:  # noqa: E501

    x_i, x_i_1 = _interval_bounds_validator(x_i, x_i_1)
    x_i_1, x_i_2 = _interval_bounds_validator(x_i_1, x_i_2)
    return (x_i, x_i_1, x_i_2)
