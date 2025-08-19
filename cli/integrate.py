import argparse
from argparse import Namespace
from typing import Callable
from nmsc._utils._helpers import _methods_dict
from nmsc._utils._helpers import _str_to_sympy_convertor
from _utils import _load_config


def _arg_parser():

    cli_cfg = _load_config("cli/configs/cli_configs.yaml")
    parser_cfg: dict = cli_cfg.get("parser", {})
    parser = argparse.ArgumentParser(
        description="Numerical integration using different methods"
    )

    parser.add_argument(
        "method",
        type=str,
        choices=parser_cfg.get("methods"),
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

    parser.add_argument("--n", type=int, help="N for romberg method only")

    parser.add_argument("--m", type=int, help="M for romberg method only")

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

    results = None
    if args.method == "romberg":
        if not args.n:
            raise ValueError("For romberg method, value of N is required to provide.")
        if not args.m:
            raise ValueError("For romberg method, value of M is required to provide.")
        results = method(f, a, b, args.n, args.m)
    else:
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
