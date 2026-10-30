# config_fingerprint

## Challenge
Return lowercase SHA-256 hex digest of canonical compact JSON for a JSON-compatible configuration, sorting dictionary keys and using UTF-8. The result must not depend on dictionary insertion order.

## Requirements
- Implement `config_fingerprint(config)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Serialize canonically before hashing.

## Run tests
`python -m pytest tests -q`
