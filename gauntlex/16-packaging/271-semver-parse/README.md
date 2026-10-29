# parse_version

## Challenge
Parse a version in exact MAJOR.MINOR.PATCH form with nonnegative decimal components and no leading zeros except 0. Return [major,minor,patch], or raise ValueError.

## Requirements
- Implement `parse_version(text)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Validate each version component before converting it to an integer.

## Run tests
`python -m pytest tests -q`
