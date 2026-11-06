# Coverage Ratio

## Description
Line coverage reports the fraction of measurable lines exercised by tests. Validate the counts and define what an empty project means.

## Requirements
- Implement `coverage_percent(covered, total)` in `starter/solution.py`.
- Accept nonnegative integer counts `covered` and `total` with `covered <= total`.
- Return the covered percentage as a float between `0.0` and `100.0`.
- Return `100.0` when `total` is zero.
- Raise `ValueError` for negative counts or when covered exceeds total.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why does an empty denominator need an explicit convention?

## Example Behavior
`coverage_percent(3, 4)` → `75.0`; `coverage_percent(0, 0)` → `100.0`.
