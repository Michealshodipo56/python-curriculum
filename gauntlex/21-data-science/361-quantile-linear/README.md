# Interpolate a Quantile

## Description
Quantiles locate positions in sorted observations, including positions that fall between two neighboring values.

## Requirements
- Implement `quantile(values, q)` in `starter/solution.py`.
- Require nonempty values and `q` between 0 and 1 inclusive.
- Sort observations without mutating input.
- Use the position `(n - 1) * q` and linearly interpolate between neighboring values when necessary.
- Raise `ValueError` for invalid `q` or empty input.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Tips
- How does an interpolated quantile differ from selecting the nearest observation?

## Example Behavior
`quantile([0, 10, 20, 30], 0.25)` → `7.5`.
