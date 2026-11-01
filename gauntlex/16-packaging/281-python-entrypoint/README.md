# Name the Entry Point

## Description
Convert a valid dotted Python module name into an executable entry-point reference.

### Behavior contract
Given a Python module path like `package.subpackage.cli`, return `package.subpackage.cli:main`. Raise ValueError for empty names or components that are not valid Python identifiers.

## Requirements
- Implement `entrypoint_name(module_name)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Each segment of a dotted name must be a valid Python identifier.

The learner must develop the implementation from the stated contract.
