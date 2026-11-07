# Compare Stable Snapshots

## Description

Structured snapshots should be compared using a canonical JSON representation so irrelevant object-key ordering does not cause false mismatches.

## Requirements

- Implement `snapshot_matches(actual, expected)` in `starter/solution.py`.
- Accept two JSON-compatible Python values.
- Compare their compact JSON representations with object keys sorted.
- Return `True` only when the canonical representations match exactly.
- Treat dictionary key order as irrelevant but list element order as significant.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why should object keys and array elements be treated differently?

## Example Behavior

`snapshot_matches({'b': 2, 'a': 1}, {'a': 1, 'b': 2})` → `True`.
