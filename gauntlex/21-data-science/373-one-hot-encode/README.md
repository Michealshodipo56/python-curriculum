# Encode Categories

## Description
Categorical labels can be represented as binary vectors with one active position. The supplied class order defines that position.

## Requirements
- Implement `one_hot_encode(labels, classes)` in `starter/solution.py`.
- Accept hashable labels and an ordered sequence of distinct classes.
- Return one row per label, with `1` at its class position and `0` elsewhere.
- Raise `ValueError` for duplicate classes or labels not found among classes.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Use the supplied class sequence as the fixed coordinate order. Reject duplicate class definitions and unknown labels rather than silently producing ambiguous or all-zero rows.

## Tips
- Why must the class order be fixed before encoding?

## Example Behavior
`one_hot_encode(['cat', 'dog'], ['dog', 'cat'])` → `[[0, 1], [1, 0]]`.
