# Weighted Observations

## Description
Calculate a mean where each value has an explicitly assigned importance.

### Behavior contract
Return sum(value*weight)/sum(weights) for equal-length nonempty lists. Weights must be nonnegative with positive total. Raise ValueError otherwise.

## Requirements
- Implement `weighted_mean(values, weights)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Reject zero total weight rather than dividing by it.

Reason about edge cases before designing your implementation.
