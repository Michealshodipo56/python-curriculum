# Move Together

## Description
Measure how two numeric series vary together around their respective means.

### Behavior contract
Return population covariance for two equal-length nonempty numeric sequences. Raise ValueError if lengths differ or are empty.

## Requirements
- Implement `population_covariance(xs, ys)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Population covariance uses the full number of observations as its divisor.

Reason about edge cases before designing your implementation.
