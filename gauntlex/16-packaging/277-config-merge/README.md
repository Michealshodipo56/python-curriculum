# Apply Overrides

## Description

Implement `merge_config(defaults, overrides)` in `starter/solution.py`. Return a new dictionary containing the defaults with recognized overrides applied.

## Requirements

- Implement `merge_config(defaults, overrides)` in `starter/solution.py`.
- Return a new dictionary containing the defaults with recognized overrides applied.
- Allow an override only if its key already exists in `defaults`.
- Ignore unknown override keys.
- Do not mutate either input mapping.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips

- **Concept to understand:** Default configuration defines which settings an application recognizes. Apply only permitted overrides and keep both source mappings intact.
- Why might allowing unknown keys unexpectedly change application behavior?

## Example Behavior

`merge_config({'port': 8000}, {'port': 9000, 'unknown': 1})` → `{'port': 9000}`.
