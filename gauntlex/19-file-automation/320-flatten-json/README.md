# Flatten a JSON Tree

## Description
Nested dictionaries can be represented by dotted paths to their leaf values. Flatten the structure without treating lists as subtrees.

## Requirements
- Implement `flatten_json(data)` in `starter/solution.py`.
- Return a dictionary mapping dotted key paths to leaf values.
- Recursively traverse dictionaries, but treat lists and empty dictionaries as leaves.
- Assume keys are nonempty strings without dots.
- Preserve original leaf values.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- Why should an empty dictionary remain visible in the flattened result?

## Example Behavior
`flatten_json({'a': {'b': 2}, 'c': []})` → `{'a.b': 2, 'c': []}`.
