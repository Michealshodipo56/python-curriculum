# Identify a Test

## Description

A test identifier combines the file location and test function name. Validate both parts before building the identifier.

## Requirements

- Implement `pytest_nodeid(path, test_name)` in `starter/solution.py`.
- Strip surrounding whitespace from `path` and `test_name`.
- Raise `ValueError` if either is empty after stripping.
- Return the exact form `path::test_name` using the trimmed parts.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why must both parts be validated before joining them?

## Example Behavior

`pytest_nodeid(' tests/test_math.py ', ' test_sum ')` → `'tests/test_math.py::test_sum'`.
