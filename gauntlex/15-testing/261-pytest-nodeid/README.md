# Identify a Test

## Description
Build a stable test identifier from a path and function name.

### Behavior contract
Return `path::test_name` for a path and test name. Raise ValueError if either is empty after stripping whitespace. Strip surrounding whitespace from both.

## Requirements
- Implement `pytest_nodeid(path, test_name)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Trim and validate both components before combining them.

Work from the contract and edge cases; do not include a finished implementation.
