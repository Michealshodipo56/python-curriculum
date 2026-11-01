# Close Enough

## Description
Compare numeric results using an allowed absolute tolerance.

### Behavior contract
Return True when absolute difference between numeric a and b is <= nonnegative tolerance; raise ValueError for negative tolerance.

## Requirements
- Implement `approx_equal(a, b, tolerance)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Exact equality can be inappropriate for floating-point calculations.

Work from the contract and edge cases; do not include a finished implementation.
