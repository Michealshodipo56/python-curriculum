# sort_requirements

## Challenge
Given valid exact requirements `name==version`, return them sorted by normalized package name, preserving the original requirement text.

## Requirements
- Implement `sort_requirements(lines)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Use normalized names as the sort key.

## Run tests
`python -m pytest tests -q`
