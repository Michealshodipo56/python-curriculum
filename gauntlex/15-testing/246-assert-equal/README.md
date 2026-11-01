# Explain a Mismatch

## Description
Create an assertion helper that clearly reports when actual and expected values differ.

### Behavior contract
Return None when actual equals expected; otherwise raise AssertionError with message `expected EXPECTED, got ACTUAL` using repr() for values.

## Requirements
- Implement `assert_equal(actual, expected)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
A useful failure message shows the values unambiguously.

Work from the contract and edge cases; do not include a finished implementation.
