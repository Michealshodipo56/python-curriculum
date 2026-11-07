# Transitive Feature Gates

## Description

A feature may be enabled by its own flag yet unavailable because a required feature is disabled. Resolve every prerequisite before reporting usable features.

## Requirements

- Implement `enabled_features(flags, dependencies)` in `starter/solution.py`.
- Accept mappings of feature flags and dependency lists.
- Include a feature only if its own flag and every transitive dependency flag are `True`.
- Treat missing flags as `False`.
- Assume dependencies are acyclic.
- Return sorted enabled feature names.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

A feature's own flag is not sufficient: every dependency in its chain must also be enabled. A missing dependency flag disables the feature.

## Tips

- Why does checking only a feature's own flag miss disabled prerequisites?

## Example Behavior

With `{'a': True, 'b': False}` and `{'a': ['b']}`, feature `a` is not enabled.
