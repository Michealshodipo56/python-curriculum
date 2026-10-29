# normalize_test_name

## Challenge
Convert a human-readable ASCII title into a pytest-style function name beginning with `test_`. Lowercase, replace each run of nonalphanumeric characters with _, and trim underscores. Return `test_unnamed` if nothing remains.

## Requirements
- Implement `normalize_test_name(title)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Normalize before adding the required test_ prefix.

## Run tests
`python -m pytest tests -q`
