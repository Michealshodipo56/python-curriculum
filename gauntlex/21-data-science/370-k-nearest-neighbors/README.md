# Find Nearby Examples

## Description
Rank data vectors by distance to a query, using original position to resolve ties.

### Behavior contract
Given a list of numeric vectors, a query vector and nonnegative integer k, return indices of the k nearest vectors by squared Euclidean distance, breaking ties by lower original index. Raise ValueError if dimensions differ or k<0. k may exceed dataset length.

## Requirements
- Implement `nearest_indices(vectors, query, k)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Squared distance preserves ordering and avoids an unnecessary square root.

Reason about edge cases before designing your implementation.
