# Explain the Variation

## Description
Evaluate predictions by comparing residual error with the variation in observed values.

### Behavior contract
Return coefficient of determination 1-SSE/SST for equal-length nonempty numeric actual and predicted sequences. When all actual values equal, return 1.0 if predictions exactly match, otherwise 0.0.

## Requirements
- Implement `r_squared(actual, predicted)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
A constant target series requires special handling.

Reason about edge cases before designing your implementation.
