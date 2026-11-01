# Compare Stable Snapshots

## Description
Decide whether two structured values have identical canonical JSON representations.

### Behavior contract
Return True if two JSON-compatible Python values have identical canonical compact sorted-key JSON representations. Dictionary key order must not matter; list order must matter.

## Requirements
- Implement `snapshot_matches(actual, expected)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Object key order is not significant, but array element order is.

Work from the contract and edge cases; do not include a finished implementation.
