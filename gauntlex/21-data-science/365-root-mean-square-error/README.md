# Penalize Large Errors

## Description
Measure prediction error with squared differences before restoring the original units.

### Behavior contract
Return square root of average squared prediction error for equal-length nonempty sequences. Raise ValueError for mismatched or empty inputs.

## Requirements
- Implement `root_mean_square_error(actual, predicted)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Squaring gives large errors more influence than small errors.

Reason about edge cases before designing your implementation.
