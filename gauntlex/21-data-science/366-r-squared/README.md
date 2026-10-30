# r_squared

## Challenge
Return coefficient of determination 1-SSE/SST for equal-length nonempty numeric actual and predicted sequences. When all actual values equal, return 1.0 if predictions exactly match, otherwise 0.0.

## Requirements
- Implement `r_squared(actual, predicted)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
SST measures variance around the actual mean.

## Run tests
`python -m pytest tests -q`
