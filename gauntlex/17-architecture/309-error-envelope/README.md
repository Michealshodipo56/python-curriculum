# Structured Errors

## Description
A consistent error response lets callers inspect an error code, message, and optional details without guessing the shape of the result.

## Requirements
- Implement `error_envelope(code, message, details)` in `starter/solution.py`.
- Accept error code, message, and optional details mapping.
- Return `{'error': {'code': code, 'message': message, 'details': details}}`.
- Use an empty dictionary when details is `None`.
- Copy provided details so later caller changes do not alter the returned response.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
The nested `details` mapping must be a new dictionary, even when the caller supplies one; a missing details argument becomes an empty mapping.

## Tips
- Why is sharing a mutable details dictionary risky?

## Example Behavior
`error_envelope('bad', 'Invalid', None)` → `{'error': {'code': 'bad', 'message': 'Invalid', 'details': {}}}`.
