# Explain the Variation

## Description
The coefficient of determination compares prediction residuals against the natural variation in the observed targets.

## Requirements
- Implement `r_squared(actual, predicted)` in `starter/solution.py`.
- Require equal-length, nonempty actual and predicted sequences.
- Compute `1 - SSE/SST` using squared residuals and squared deviations from the actual mean.
- If all actual values are equal, return `1.0` for exact predictions and `0.0` otherwise.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Compare residual error against variation around the actual mean. A constant target has no natural variation, so use the specified exact-prediction rule instead of dividing by zero.

## Tips
- Why does a constant target sequence require a special rule?

## Example Behavior
`r_squared([1, 2, 3], [1, 2, 3])` → `1.0`.
