# lower_bound

## Challenge
Return the first index in sorted ascending values where element >= target, or len(values) if none. Duplicates are allowed. Must use O(log n) comparisons.

## Requirements
- Implement `lower_bound(values, target)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Hint
Maintain a half-open search interval.

## Run tests
`python -m pytest tests -q`
