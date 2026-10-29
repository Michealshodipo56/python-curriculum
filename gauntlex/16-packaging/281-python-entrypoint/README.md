# entrypoint_name

## Challenge
Given a Python module path like `package.subpackage.cli`, return `package.subpackage.cli:main`. Raise ValueError for empty names or components that are not valid Python identifiers.

## Requirements
- Implement `entrypoint_name(module_name)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Validate each dot-separated component with identifier rules.

## Run tests
`python -m pytest tests -q`
