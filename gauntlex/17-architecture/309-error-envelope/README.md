# Structured Errors

## Description
Wrap an error code and message in a consistent response shape with independent details.

### Behavior contract
Return {'error':{'code':code,'message':message,'details':details}}. If details is None, use an empty dictionary. Copy details to avoid aliasing caller data.

## Requirements
- Implement `error_envelope(code, message, details)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Copy mutable details rather than sharing caller-owned state.

Design your own implementation from the specified behavior.
