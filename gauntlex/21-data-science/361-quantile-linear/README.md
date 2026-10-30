# quantile

## Challenge
Return a quantile for nonempty numeric values and q in [0,1], using sorted values and linear interpolation at position (n-1)*q. Raise ValueError for invalid q or empty values.

## Requirements
- Implement `quantile(values, q)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Interpolate between the two neighboring sorted positions.

## Run tests
`python -m pytest tests -q`
