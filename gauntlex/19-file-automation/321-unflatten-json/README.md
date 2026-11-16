# Rebuild Nested JSON

## Description

Implement `unflatten_json(data)` in `starter/solution.py`. Construct nested dictionaries for intermediate path components.

## Requirements

- Implement `unflatten_json(data)` in `starter/solution.py`.
- Accept flat keys made of nonempty dot-separated components.
- Construct nested dictionaries for intermediate path components.
- Assign each original leaf value at its final component.
- Assume no conflicting paths such as `a` and `a.b`.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations

Build intermediate dictionaries only for nonfinal path components, then place the supplied leaf at its terminal key. Rely on the stated absence of prefix conflicts rather than inventing a conflict policy.

## Tips

- **Concept to understand:** Reverse a flat mapping of dotted paths into nested dictionaries, creating intermediate containers only where needed.
- What intermediate structure is needed for a key with three components?

## Example Behavior

`unflatten_json({'a.b': 2, 'a.c': 3})` → `{'a': {'b': 2, 'c': 3}}`.
