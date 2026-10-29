# wheel_name

## Challenge
Given normalized package name, version, and Python tag, return `NAME-VERSION-TAG-none-any.whl`. Convert hyphens in the package name to underscores. Inputs are trusted nonempty strings.

## Requirements
- Implement `wheel_name(name, version, python_tag)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Wheel filenames use underscores in the distribution component.

## Run tests
`python -m pytest tests -q`
