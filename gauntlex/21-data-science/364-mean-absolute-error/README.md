# Average Prediction Error

## Description
Measure the typical magnitude of a prediction's error without cancellation.

### Behavior contract
Return average absolute difference between corresponding numeric actual and predicted values. Require equal nonempty lengths, otherwise raise ValueError.

## Requirements
- Implement `mean_absolute_error(actual, predicted)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Errors on opposite sides of the truth must not cancel each other.

Reason about edge cases before designing your implementation.
