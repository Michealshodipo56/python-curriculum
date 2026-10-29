# merge_config

## Challenge
Return a new dictionary formed by applying environment overrides to default settings. Only keys present in defaults may be overridden; unknown keys are ignored. Neither input may be mutated.

## Requirements
- Implement `merge_config(defaults, overrides)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Start from a copy of the defaults.

## Run tests
`python -m pytest tests -q`
