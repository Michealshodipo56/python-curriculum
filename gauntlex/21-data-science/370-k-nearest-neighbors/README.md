# Find Nearby Examples

## Description
Nearest-neighbor search ranks examples by their distance from a query, with deterministic tie-breaking.

## Requirements
- Implement `nearest_indices(vectors, query, k)` in `starter/solution.py`.
- Accept a list of numeric vectors, a query vector, and nonnegative integer `k`.
- Compare each vector using squared Euclidean distance to the query.
- Return indices of the nearest `k` vectors, breaking equal-distance ties by lower original index.
- Raise `ValueError` for mismatched dimensions or negative `k`; allow `k` greater than the dataset length.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Rank each candidate by squared Euclidean distance, using its original index as a deterministic tie-breaker. If `k` exceeds the dataset size, return every candidate in ranked order.

## Tips
- Why is the square root unnecessary when ranking distances?

## Example Behavior
`nearest_indices([[0], [2], [4]], [3], 2)` → `[1, 2]`.
