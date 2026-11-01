# Standardize Observations

## Description
Transform values relative to their population mean and standard deviation.

### Behavior contract
Standardize a list of numeric values using population standard deviation (divide variance by n). Return [] for empty input, and all zeros for zero variance.

## Requirements
- Implement `z_score_scale(values)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
A zero-variance dataset requires a defined result.

Reason about edge cases before designing your implementation.
