# Three-Part Version

## Description

Package releases often use three numeric components: major, minor, and patch. Parse this precise version form without silently accepting ambiguous formatting.

## Requirements

- Implement `parse_version(text)` in `starter/solution.py`.
- Accept exactly `MAJOR.MINOR.PATCH` with three nonnegative decimal integers.
- Reject leading zeros in multi-digit components; `0` itself is valid.
- Return `[major, minor, patch]` as integers.
- Raise `ValueError` for missing, extra, negative, or malformed components.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips

- Why is strict validation preferable to guessing what a malformed version means?

## Example Behavior

`parse_version('2.10.3')` → `[2, 10, 3]`; `parse_version('01.2.3')` raises `ValueError`.
