"""
Module for validating functions of type R -> R.

Functions:
    _R_to_R_func_validator: Validates that a function takes and returns a float.
"""

import inspect
from typing import Callable
from pydantic import validate_call


@validate_call(validate_return=True)
def _R_to_R_func_validator(func: Callable[[float], float]) -> Callable[[float], float]:

    sig = inspect.signature(func)
    params = list(sig.parameters.values())

    # Must take exactly one argument
    if len(params) != 1:
        raise ValueError(
            "Function func must take exactly one argument, "
            f"instead it is accepting {len(params)} arguments."
        )

    # Argument must be annotated as float
    if params[0].annotation is not float:
        raise TypeError(
            "Only argument of function func must be of type float, "
            f"but instead it is {params[0].annotation}"
        )

    # Return type must be float
    if sig.return_annotation is not float:
        raise TypeError(
            "Return type of function func must be of type float, "
            f"but instead it is {sig.return_annotation}"
        )

    return func
