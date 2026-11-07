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

## Design Considerations

Differentiate an empty mapping from a nonempty mapping: an empty dictionary is a leaf that must survive flattening. Lists are also opaque values, even when they contain dictionaries.

## Tips

- Why should an empty dictionary remain visible in the flattened result?

## Example Behavior

`flatten_json({'a': {'b': 2}, 'c': []})` → `{'a.b': 2, 'c': []}`.
