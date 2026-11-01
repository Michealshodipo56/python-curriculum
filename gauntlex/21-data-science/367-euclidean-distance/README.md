# Straight-Line Distance

## Description
Measure geometric distance between numeric vectors of equal length.

### Behavior contract
Return Euclidean distance between equal-length numeric vectors. Empty vectors have distance 0. Raise ValueError for different lengths.

## Requirements
- Implement `euclidean_distance(a, b)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Dimension mismatch is an invalid comparison.

Reason about edge cases before designing your implementation.
