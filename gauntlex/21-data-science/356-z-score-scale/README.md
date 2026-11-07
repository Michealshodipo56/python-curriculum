# Standardize Observations

## Description

Express each observation relative to the population's center and spread, rather than its original units.

## Requirements

- Implement `z_score_scale(values)` in `starter/solution.py`.
- Calculate the population mean and population standard deviation (variance divided by `n`).
- Return each value's deviation from the mean divided by that standard deviation.
- Return `[]` for empty input and zeros for zero variance.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations

Use population variance with divisor `n`, not sample variance with `n-1`. If every observation equals the mean, return a zero for each position instead of dividing by zero.

## Tips

- How does population variance differ from sample variance?

## Example Behavior

`z_score_scale([2, 2, 2])` → `[0.0, 0.0, 0.0]`.
