from typing import Callable
from pydantic import validate_call
from sympy import sympify, lambdify, SympifyError, Expr, Symbol


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
