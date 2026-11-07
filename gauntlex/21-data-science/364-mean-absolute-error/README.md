# Average Prediction Error

## Description
Prediction errors above and below the target should not cancel. Measure the average magnitude of deviations.

## Requirements
- Implement `mean_absolute_error(actual, predicted)` in `starter/solution.py`.
- Require equal-length, nonempty actual and predicted sequences.
- Compute absolute differences for corresponding observations.
- Return their arithmetic mean.
- Raise `ValueError` for empty or mismatched sequences.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Take the absolute magnitude of each paired residual before averaging, so overprediction and underprediction cannot cancel. Require at least one matched observation.

## Tips
- Why is taking absolute values necessary before averaging?

## Example Behavior
`mean_absolute_error([1, 3], [2, 1])` → `1.5`.
