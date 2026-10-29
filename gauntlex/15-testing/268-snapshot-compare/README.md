# snapshot_matches

## Challenge
Return True if two JSON-compatible Python values have identical canonical compact sorted-key JSON representations. Dictionary key order must not matter; list order must matter.

## Requirements
- Implement `snapshot_matches(actual, expected)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Canonical JSON serialization gives stable snapshots.

## Run tests
`python -m pytest tests -q`
