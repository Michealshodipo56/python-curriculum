# What Changed?

## Description

Compare an older collection of labels with a newer collection. Report which distinct values were introduced, removed, or kept.

## Requirements

- Implement `set_diff(old, new)` in `starter/solution.py`.
- Accept two collections of strings named `old` and `new`.
- Ignore duplicate occurrences within each collection.
- Return a dictionary with exactly `added`, `removed`, and `shared` keys.
- Each value must be a sorted list of strings.
- `added` contains only new values; `removed` contains only old values; `shared` contains values in both.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why does comparison direction matter?
- How should duplicates affect membership and the result?

## Example Behavior

`set_diff(['a', 'b'], ['b', 'c'])` → `{'added': ['c'], 'removed': ['a'], 'shared': ['b']}`.
