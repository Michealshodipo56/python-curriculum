# City-Block Distance

## Description
Sum absolute coordinate differences between two vectors.

### Behavior contract
Return the sum of absolute coordinate differences between equal-length numeric vectors. Empty vectors return 0; mismatched lengths raise ValueError.

## Requirements
- Implement `manhattan_distance(a, b)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Unlike Euclidean distance, this measure does not square differences.

Reason about edge cases before designing your implementation.
