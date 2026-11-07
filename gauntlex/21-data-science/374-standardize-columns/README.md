# Normalize Each Feature

## Description
Different features can have different scales. Standardize each matrix column independently using population statistics.

## Requirements
- Implement `standardize_columns(matrix)` in `starter/solution.py`.
- Accept a rectangular matrix of numeric rows.
- Compute each column's population mean and standard deviation.
- Standardize each column independently; replace constant columns with zeros.
- Return `[]` for an empty matrix; raise `ValueError` for ragged rows.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Tips
- Why would computing one mean for the entire matrix distort individual features?

## Example Behavior
`standardize_columns([[1, 10], [3, 10]])` → `[[-1.0, 0.0], [1.0, 0.0]]`.
