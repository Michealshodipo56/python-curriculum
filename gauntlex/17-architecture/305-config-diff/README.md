# Configuration Changes

## Description
Configuration drift can come from changed values, added settings, or removed settings. Report every key that differs between two snapshots.

## Requirements
- Implement `config_diff(old, new)` in `starter/solution.py`.
- Accept old and new dictionaries.
- Return sorted keys whose values differ or whose presence differs.
- Treat a missing key as different from a present key whose value is `None`.
- Do not mutate either dictionary.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A missing key is not equivalent to a present key whose value is `None`; report the key as changed.

## Tips
- Why is missing different from explicitly configured `None`?

## Example Behavior
`config_diff({'a': None}, {})` → `['a']`.
