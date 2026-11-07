# Package Metadata

## Description

Build a small package metadata record that does not unexpectedly change when the caller later edits its dependency list.

## Requirements

- Implement `build_metadata(name, version, minimum_python, dependencies)` in `starter/solution.py`.
- Return a dictionary with keys `name`, `version`, `requires_python`, and `dependencies`.
- Set `requires_python` from `minimum_python`.
- Copy the supplied dependency list into the result.
- Do not mutate the input list or retain it by reference.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips

- Why can sharing a mutable dependency list cause unexpected changes after the function returns?

## Example Behavior

`build_metadata('demo', '1.0.0', '>=3.10', ['requests'])` returns the four metadata fields and an independent dependency list.
