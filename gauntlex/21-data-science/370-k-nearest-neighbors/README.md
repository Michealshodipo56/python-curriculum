# nearest_indices

## Challenge
Given a list of numeric vectors, a query vector and nonnegative integer k, return indices of the k nearest vectors by squared Euclidean distance, breaking ties by lower original index. Raise ValueError if dimensions differ or k<0. k may exceed dataset length.

## Requirements
- Implement `nearest_indices(vectors, query, k)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Squared distances preserve ordering without a square root.

## Run tests
`python -m pytest tests -q`
