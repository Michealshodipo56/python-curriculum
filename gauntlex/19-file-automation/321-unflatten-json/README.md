# Rebuild Nested JSON

## Description
Reverse a flat mapping of dotted paths into nested dictionaries, creating intermediate containers only where needed.

## Requirements
- Implement `unflatten_json(data)` in `starter/solution.py`.
- Accept flat keys made of nonempty dot-separated components.
- Construct nested dictionaries for intermediate path components.
- Assign each original leaf value at its final component.
- Assume no conflicting paths such as `a` and `a.b`.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- What intermediate structure is needed for a key with three components?

## Example Behavior
`unflatten_json({'a.b': 2, 'a.c': 3})` → `{'a': {'b': 2, 'c': 3}}`.
