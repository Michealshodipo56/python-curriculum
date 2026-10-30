# population_covariance

## Challenge
Return population covariance for two equal-length nonempty numeric sequences. Raise ValueError if lengths differ or are empty.

## Requirements
- Implement `population_covariance(xs, ys)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Center both series around their means.

## Run tests
`python -m pytest tests -q`
