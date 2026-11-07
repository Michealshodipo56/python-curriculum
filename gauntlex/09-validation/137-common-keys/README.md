# Shared Dictionary Keys

## Description

Two dictionaries may contain some of the same keys even when their values differ. Find the shared keys and return them in a predictable order.

## Requirements

- Implement `common_keys(a, b)` in `starter/solution.py`.
- Accept two dictionaries with sortable string keys.
- Return a sorted list of keys present in both dictionaries.
- Ignore the values associated with those keys.
- Return `[]` when no keys are shared; do not modify either dictionary.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why should different values not affect whether keys match?
- How does sorting remove dependence on insertion order?

## Example Behavior

`common_keys({'x': 1, 'a': 2}, {'a': 3, 'z': 4})` → `['a']`; `common_keys({}, {'x': 1})` → `[]`.
