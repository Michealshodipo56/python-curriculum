# Weighted Recent History

## Description
Exponential smoothing balances a new observation with the previous smoothed estimate, producing a history-aware series.

## Requirements
- Implement `exponential_smoothing(values, alpha)` in `starter/solution.py`.
- Require smoothing factor `alpha` to satisfy `0 < alpha <= 1`.
- For nonempty input, begin with the first observation unchanged.
- For later observations, combine the current value and previous smoothed output using `alpha` and `1-alpha`.
- Return `[]` for empty input.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Initialize the smoothed sequence from the first observation, then combine each later raw value with the previous smoothed result. The parameter bounds keep the recurrence meaningful.

## Tips
- Why must the recurrence use the previous smoothed value rather than the previous raw observation?

## Example Behavior
`exponential_smoothing([10, 20, 30], 0.5)` → `[10, 15.0, 22.5]`.
