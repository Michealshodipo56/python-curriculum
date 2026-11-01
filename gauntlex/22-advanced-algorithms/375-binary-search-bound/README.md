# First Not Smaller

## Description
Find the earliest position where a sorted value meets or exceeds a target using logarithmic comparisons.

### Behavior contract
Return the first index in sorted ascending values where element >= target, or len(values) if none. Duplicates are allowed. Must use O(log n) comparisons.

## Requirements
- Implement `lower_bound(values, target)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Tips
Maintain a search interval whose boundaries have a precise meaning.

The task is to design an implementation that meets both behavior and efficiency requirements.
