# Apply Overrides

## Description
Combine default settings with recognized overrides without changing either input.

### Behavior contract
Return a new dictionary formed by applying environment overrides to default settings. Only keys present in defaults may be overridden; unknown keys are ignored. Neither input may be mutated.

## Requirements
- Implement `merge_config(defaults, overrides)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Unknown keys must not unexpectedly expand the configuration.

The learner must develop the implementation from the stated contract.
