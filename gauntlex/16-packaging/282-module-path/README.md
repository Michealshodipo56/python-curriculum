# module_to_path

## Challenge
Convert a dotted Python module name into a relative POSIX path ending in .py. Raise ValueError for invalid identifier components.

## Requirements
- Implement `module_to_path(module_name)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Split on dots, validate identifiers, and join with forward slashes.

## Run tests
`python -m pytest tests -q`
