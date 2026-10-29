# config_diff

## Challenge
Return a sorted list of keys whose values differ between old and new dictionaries. Treat missing keys as different from present keys, even when the present value is None.

## Requirements
- Implement `config_diff(old, new)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
A sentinel distinguishes missing keys from None values.

## Run tests
`python -m pytest tests -q`
