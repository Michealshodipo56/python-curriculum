# First Strictly Greater

## Description
Find the earliest position where a sorted value is greater than a target.

### Behavior contract
Return the first index in sorted ascending values where element > target, or len(values) if none. Must use O(log n) comparisons.

## Requirements
- Implement `upper_bound(values, target)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Tips
Equality changes which half of the search interval can be discarded.

The task is to design an implementation that meets both behavior and efficiency requirements.
