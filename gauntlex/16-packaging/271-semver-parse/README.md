# Three-Part Version

## Description
Validate and interpret a version made of major, minor, and patch numbers.

### Behavior contract
Parse a version in exact MAJOR.MINOR.PATCH form with nonnegative decimal components and no leading zeros except 0. Return [major,minor,patch], or raise ValueError.

## Requirements
- Implement `parse_version(text)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Reject malformed versions rather than trying to guess their meaning.

The learner must develop the implementation from the stated contract.
