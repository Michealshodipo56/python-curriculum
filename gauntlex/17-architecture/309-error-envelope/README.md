# error_envelope

## Challenge
Return {'error':{'code':code,'message':message,'details':details}}. If details is None, use an empty dictionary. Copy details to avoid aliasing caller data.

## Requirements
- Implement `error_envelope(code, message, details)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Use a fresh details dictionary.

## Run tests
`python -m pytest tests -q`
