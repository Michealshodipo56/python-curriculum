# Compare Directions

## Description
Cosine similarity compares vector orientation rather than raw distance, making direction the focus of the measure.

## Requirements
- Implement `cosine_similarity(a, b)` in `starter/solution.py`.
- Require equal-length vectors, or raise `ValueError`.
- Compute the dot product divided by the product of vector magnitudes.
- Return `0.0` when either magnitude is zero, including empty vectors.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Calculate directional similarity from a dot product and the two vector magnitudes. A zero-magnitude vector has no defined direction, so return the prescribed zero result.

## Tips
- Why is a zero vector a special case for directional similarity?

## Example Behavior
`cosine_similarity([1, 0], [0, 1])` → `0.0`; identical unit vectors → `1.0`.
