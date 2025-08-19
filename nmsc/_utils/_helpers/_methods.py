from nmsc.methods import (
    trapezoidal,
    midpoint,
    simpson,
    romberg,
)

_methods_dict = {
    "trapezoidal": trapezoidal,
    "midpoint": midpoint,
    "simpson": simpson,
    "romberg": romberg,
}
