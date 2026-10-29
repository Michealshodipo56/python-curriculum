# pytest_nodeid

## Challenge
Return `path::test_name` for a path and test name. Raise ValueError if either is empty after stripping whitespace. Strip surrounding whitespace from both.

## Requirements
- Implement `pytest_nodeid(path, test_name)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Validate the components before joining them.

## Run tests
`python -m pytest tests -q`
