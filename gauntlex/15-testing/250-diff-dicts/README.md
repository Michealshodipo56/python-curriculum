# Compare Records

## Description

Two records can differ because a field was added, removed, or changed. Report every difference without losing which side contained which value.

## Requirements

- Implement `diff_dicts(old, new)` in `starter/solution.py`.
- Accept `old` and `new` mappings whose stored values are never `None`.
- Include every key appearing in either mapping whose values differ or whose key is missing on one side.
- Return a dictionary mapping each changed key to `[old_value, new_value]`.
- Use `None` for an absent side; omit unchanged keys.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why is it important to distinguish a missing key from an equal value?

## Example Behavior

`diff_dicts({'a': 1}, {'a': 2, 'b': 3})` → `{'a': [1, 2], 'b': [None, 3]}`.
