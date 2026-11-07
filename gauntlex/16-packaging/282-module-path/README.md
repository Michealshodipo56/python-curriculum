# Module to File

## Description
A Python module's dotted import path corresponds to directories and a source filename. Convert the module name into a relative POSIX file path.

## Requirements
- Implement `module_to_path(module_name)` in `starter/solution.py`.
- Accept a dotted module name.
- Require every component to be a valid Python identifier.
- Replace module separators with forward slashes and append `.py`.
- Raise `ValueError` for empty or invalid components.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why must dots become path separators rather than remain in the filename?

## Example Behavior
`module_to_path('package.tools.cli')` → `'package/tools/cli.py'`.
