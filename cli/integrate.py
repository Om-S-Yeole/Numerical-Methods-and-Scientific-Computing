import argparse
from argparse import Namespace
from typing import Callable
from pydantic import validate_call
from sympy import sympify, lambdify, SympifyError, Expr, Symbol
from nmsc._utils._helpers import _methods_dict


@validate_call(validate_return=True)
def _str_to_sympy_convertor(expr_str: str) -> Callable[[float], float]:
    if not isinstance(expr_str, str):
        raise TypeError(
            f"Expected type of expr_str is str, instead got {type(expr_str)}"
        )
    expr: Expr | None = None
    try:
        expr: Expr = sympify(expr_str, convert_xor=True, rational=False)
    except SympifyError as e:
        raise ValueError("Invalid input mathematical expression") from e
    if len(expr.free_symbols) != 1:
        raise ValueError(
            "It is expected that mathematical function provided must contain exactly "
            f"one variable. Instead got {len(expr.free_symbols)} "
            f"variables that are {expr.free_symbols}"
        )

    var: Symbol = expr.free_symbols.pop()
    func = lambdify(var, expr, "numpy")

    def mathematical_expression(x: float) -> float:
        result: float = float(func(x))
        return result

    return mathematical_expression


def _arg_parser():
    parser = argparse.ArgumentParser(
        description="Numerical integration using different methods"
    )

    parser.add_argument(
        "method",
        type=str,
        choices=["trapezoidal"],
        default=["trapezoidal"],
        help="Name of the numerical integration method",
    )

    parser.add_argument(
        "f",
        type=str,
        help="Mathematical function for which numerical integration is to be done. Must contain exactly one variable.",  # noqa: E501
    )

    parser.add_argument("a", type=float, help="Lower bound of integration")

    parser.add_argument("b", type=float, help="Upper bound of integration")

    parser.add_argument(
        "--grid_pts", type=int, help="Number of grid points", default=50
    )

    parser.add_argument(
        "--req_time",
        action="store_true",
        required=False,
        help="Whether to return the time required for computation of the method",
    )

    args: Namespace = parser.parse_args()
    return args


def main():
    args: Namespace = _arg_parser()
    method = _methods_dict.get(args.method, None)
    if method is None:
        raise ValueError(f"Invalid input for method. Got {args.method}")
    f: Callable[[float], float] = _str_to_sympy_convertor(args.f)
    a: float = args.a
    b: float = args.b
    grid_pts = args.grid_pts
    req_time = args.req_time

    results = method(f, a, b, grid_pts)

    print("====== Results ======")
    print(f"Method: {args.method}")
    print(f"a = {args.a}")
    print(f"b = {args.b}")
    print(f"grid_pts = {args.grid_pts}")
    print("---------------------")
    print(f"Computed integral value: {results.integral}")
    if req_time:
        print(f"Time required: {results.req_time} s")
    print("=====================")


if __name__ == "__main__":
    main()
