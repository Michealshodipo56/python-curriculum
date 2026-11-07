# Move Together

## Description
Covariance describes whether two series tend to rise and fall together relative to their own means.

## Requirements
- Implement `population_covariance(xs, ys)` in `starter/solution.py`.
- Require equal-length, nonempty numeric sequences.
- Compute each series' mean and sum paired deviations' products.
- Divide by the full number of observations for population covariance.
- Raise `ValueError` for empty or mismatched inputs.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Pair observations by index, measure both deviations from their respective means, and divide the aggregate by the population count. Reject empty and unequal-length series.

## Tips
- Why is the population divisor `n` instead of `n-1`?

## Example Behavior
`population_covariance([1, 2, 3], [2, 4, 6])` → approximately `1.3333333333`.
