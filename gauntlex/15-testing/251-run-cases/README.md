# Evaluate Examples

## Description
Run a collection of input-output cases against a callable and report which ones match.

### Behavior contract
Given a callable fn and list of [args,expected] cases where args is a list, return a list of booleans indicating whether fn(*args) equals expected. Let exceptions propagate.

## Requirements
- Implement `run_cases(fn, cases)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Keep each result aligned with its original case.

Work from the contract and edge cases; do not include a finished implementation.
