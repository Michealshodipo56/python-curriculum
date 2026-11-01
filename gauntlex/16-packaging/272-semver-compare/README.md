# Version Ordering

## Description
Compare two three-part versions according to numeric component precedence.

### Behavior contract
Compare two valid MAJOR.MINOR.PATCH versions; return -1, 0, or 1. Versions have no prerelease or build suffixes.

## Requirements
- Implement `compare_version(a, b)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Version 1.10.0 is newer than 1.9.0 despite their string order.

The learner must develop the implementation from the stated contract.
