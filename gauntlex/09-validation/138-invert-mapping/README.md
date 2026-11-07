# Reverse a Relationship

## Description
A dictionary can map several keys to the same value. Reverse that relationship while preserving every original key and its encounter order.

## Requirements
- Implement `invert_mapping(mapping)` in `starter/solution.py`.
- Accept a dictionary mapping strings to strings.
- Return a new dictionary whose keys are the original values.
- Associate each new key with a list of original keys having that value.
- Preserve the original dictionary's key insertion order within each list.
- Return `{}` for an empty mapping.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why might an inverted mapping need lists rather than single values?
- What ordering should be preserved when multiple keys share a value?

## Example Behavior
`invert_mapping({'a': 'x', 'b': 'y', 'c': 'x'})` → `{'x': ['a', 'c'], 'y': ['b']}`.
