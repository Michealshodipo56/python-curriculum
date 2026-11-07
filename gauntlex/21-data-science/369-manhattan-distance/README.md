# City-Block Distance

## Description
Some distances are measured by adding coordinate-wise travel rather than following a straight line.

## Requirements
- Implement `manhattan_distance(a, b)` in `starter/solution.py`.
- Require equal-length numeric vectors; raise `ValueError` on mismatch.
- Return the sum of absolute differences between corresponding coordinates.
- Return `0` for two empty vectors.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Add absolute coordinate differences rather than squaring them. The result represents axis-aligned travel and is defined as zero for two empty vectors.

## Tips
- How does this distance differ from Euclidean distance on a two-dimensional grid?

## Example Behavior
`manhattan_distance([0, 0], [3, 4])` → `7`.
