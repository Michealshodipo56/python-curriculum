# weighted_mean

## Challenge
Return sum(value*weight)/sum(weights) for equal-length nonempty lists. Weights must be nonnegative with positive total. Raise ValueError otherwise.

## Requirements
- Implement `weighted_mean(values, weights)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Validate shape and total weight before division.

## Run tests
`python -m pytest tests -q`
