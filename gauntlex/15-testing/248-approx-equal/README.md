# Close Enough

## Description
Floating-point results may differ slightly because of representation and rounding. Compare numbers using an explicit absolute tolerance.

## Requirements
- Implement `approx_equal(a, b, tolerance)` in `starter/solution.py`.
- Accept numeric `a`, `b`, and a nonnegative `tolerance`.
- Return `True` when their absolute difference is at most the tolerance; otherwise return `False`.
- Raise `ValueError` for a negative tolerance.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is exact equality sometimes inappropriate for floating-point calculations?

## Example Behavior
`approx_equal(1.01, 1.0, 0.02)` → `True`; `approx_equal(1.1, 1.0, 0.01)` → `False`.
