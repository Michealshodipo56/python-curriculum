# parse_requirement

## Challenge
Parse an exact requirement `name==version`, where name contains ASCII letters, digits, underscores or hyphens, and version has three dot-separated nonnegative integers. Return [normalized_name,version], where name is lowercase with underscores replaced by hyphens. Raise ValueError on invalid input.

## Requirements
- Implement `parse_requirement(text)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Separate name normalization from version validation.

## Run tests
`python -m pytest tests -q`
