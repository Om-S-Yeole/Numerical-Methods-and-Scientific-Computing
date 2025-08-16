"""
Module for validating grid points for numerical methods.

Functions:
    _grid_pts_validator: Validates the number of grid points is within bounds.
"""

from pydantic import validate_call


@validate_call(validate_return=True)
def _grid_pts_validator(
    grid_pts: int, min_grid_pts: int, max_grid_pts: int = 200000
) -> int:

    if grid_pts < min_grid_pts:
        raise ValueError(
            f"Number of grid points must be greater than {min_grid_pts}. "
            f"Received value of argument grid_pts is {grid_pts}"
        )
    if grid_pts > max_grid_pts:
        raise ValueError(
            "Number of grid points are restricted to be lesser than "
            f"{max_grid_pts} in order to avoid memory overflow"
        )

    return grid_pts
