# Name the Entry Point

## Description
A command-line entry point refers to a Python module and the function to execute. Validate a dotted module path before adding the function reference.

## Requirements
- Implement `entrypoint_name(module_name)` in `starter/solution.py`.
- Accept a nonempty dotted module name.
- Require every dot-separated component to be a valid Python identifier.
- Return `module.path:main` using the original valid module name.
- Raise `ValueError` for empty names or invalid components.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why is validating each component more reliable than checking only the full string?

## Example Behavior
`entrypoint_name('package.cli')` → `'package.cli:main'`; `entrypoint_name('package..cli')` raises `ValueError`.
