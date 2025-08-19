from pydantic import validate_call


@validate_call(validate_return=True)
def _romberg_hyperparameters_validator(n: int, m: int) -> tuple[int, int]:
    if (n < 0) or (m < 0):
        raise ValueError(
            f"Values of N and M are not allwed to be less than 0. Got N={n}, M={m}"
        )
    return (n, m)
