# Structured Errors

## Description

Implement `error_envelope(code, message, details)` in `starter/solution.py`. Return `{'error': {'code': code, 'message': message, 'details': details}}`.

## Requirements

- Implement `error_envelope(code, message, details)` in `starter/solution.py`.
- Accept error code, message, and a required third argument `details`, which may be a mapping or `None`.
- Return `{'error': {'code': code, 'message': message, 'details': details}}`.
- Use an empty dictionary when details is `None`.
- Copy provided details so later caller changes do not alter the returned response.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

The nested `details` mapping must be a new dictionary, even when the caller supplies one; `details=None` becomes an empty mapping.

## Tips

- **Concept to understand:** A consistent error response lets callers inspect an error code, message, and optional details without guessing the shape of the result.
- Why is sharing a mutable details dictionary risky?

## Example Behavior

`error_envelope('bad', 'Invalid', None)` → `{'error': {'code': 'bad', 'message': 'Invalid', 'details': {}}}`.
