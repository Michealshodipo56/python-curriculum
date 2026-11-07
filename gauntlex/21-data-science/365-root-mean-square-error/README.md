# Penalize Large Errors

## Description
Squaring prediction errors makes larger deviations contribute more strongly to the overall error score.

## Requirements
- Implement `root_mean_square_error(actual, predicted)` in `starter/solution.py`.
- Require nonempty actual and predicted numeric sequences of equal length.
- Square each paired prediction difference, average those squares, and return the square root.
- Raise `ValueError` for empty or mismatched sequences.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Tips
- Why does squaring make large errors more influential?

## Example Behavior
`root_mean_square_error([0, 0], [3, 4])` → approximately `3.5355339`.
