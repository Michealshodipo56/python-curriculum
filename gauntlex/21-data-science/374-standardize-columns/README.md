# Normalize Each Feature

## Description
Standardize every feature column independently across a matrix of observations.

### Behavior contract
Given a rectangular matrix of numeric rows, standardize each column independently using population mean and standard deviation. Constant columns become zeros. Return [] for empty matrix; raise ValueError for ragged rows.

## Requirements
- Implement `standardize_columns(matrix)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Different columns can have different means and spreads.

Reason about edge cases before designing your implementation.
