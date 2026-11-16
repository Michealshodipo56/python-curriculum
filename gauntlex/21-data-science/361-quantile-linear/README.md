# Interpolate a Quantile

## Description

Implement `quantile(values, q)` in `starter/solution.py`. Require nonempty values and `q` between 0 and 1 inclusive.

## Requirements

- Implement `quantile(values, q)` in `starter/solution.py`.
- Require nonempty values and `q` between 0 and 1 inclusive.
- Sort observations without mutating input.
- Use the position `(n - 1) * q` and linearly interpolate between neighboring values when necessary.
- Raise `ValueError` for invalid `q` or empty input.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations

Sort a copy of the data before locating the fractional index `(n - 1) * q`. When the position lies between observations, interpolate rather than rounding to a nearby index.

## Tips

- **Concept to understand:** Quantiles locate positions in sorted observations, including positions that fall between two neighboring values.
- How does an interpolated quantile differ from selecting the nearest observation?

## Example Behavior

`quantile([0, 10, 20, 30], 0.25)` → `7.5`.
