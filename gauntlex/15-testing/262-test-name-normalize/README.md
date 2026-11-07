# Name a Test Function

## Description
Turn a human-readable ASCII title into a predictable pytest-style function name, avoiding repeated or trailing separators.

## Requirements
- Implement `normalize_test_name(title)` in `starter/solution.py`.
- Lowercase the ASCII title.
- Replace each run of nonalphanumeric characters with one underscore.
- Trim leading and trailing underscores from the normalized title.
- Prefix the result with `test_`, or return `test_unnamed` when no alphanumeric characters remain.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why should consecutive punctuation marks become a single separator?

## Example Behavior
`normalize_test_name('  Save & Load! ')` → `'test_save_load'`; `normalize_test_name('!!!')` → `'test_unnamed'`.
