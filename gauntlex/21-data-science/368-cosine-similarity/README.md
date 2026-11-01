# Compare Directions

## Description
Measure vector similarity by the angle between two numeric vectors.

### Behavior contract
Return cosine similarity of equal-length numeric vectors. Return 0.0 if either vector has zero magnitude, including empty vectors. Raise ValueError on length mismatch.

## Requirements
- Implement `cosine_similarity(a, b)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
A zero-length vector has no direction; the task defines a fallback.

Reason about edge cases before designing your implementation.
