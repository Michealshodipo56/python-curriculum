# Weighted Observations

## Description

Some observations contribute more to a summary than others. Compute a mean that respects their supplied nonnegative weights.

## Requirements

- Implement `weighted_mean(values, weights)` in `starter/solution.py`.
- Require equal-length nonempty value and weight sequences; otherwise raise `ValueError`.
- Reject negative weights and a zero total weight with `ValueError`.
- Return the sum of value-times-weight products divided by the sum of weights.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations

Validate that values and weights align and that the total weight is positive. Zero-weight observations are allowed, but negative weights and an all-zero weighting are not.

## Tips

- What happens if every weight is zero?

## Example Behavior

`weighted_mean([10, 20], [1, 3])` → `17.5`.
