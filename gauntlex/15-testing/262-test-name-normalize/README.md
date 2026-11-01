# Name a Test Function

## Description
Turn a human-readable title into a valid, consistent test function name.

### Behavior contract
Convert a human-readable ASCII title into a pytest-style function name beginning with `test_`. Lowercase, replace each run of nonalphanumeric characters with _, and trim underscores. Return `test_unnamed` if nothing remains.

## Requirements
- Implement `normalize_test_name(title)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Punctuation and repeated separators should not create messy identifiers.

Work from the contract and edge cases; do not include a finished implementation.
