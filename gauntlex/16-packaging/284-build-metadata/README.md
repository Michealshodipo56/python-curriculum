# build_metadata

## Challenge
Return a dictionary with keys name, version, requires_python, dependencies from name, version, minimum_python, and dependency list. Copy the dependencies list so caller changes do not affect the result.

## Requirements
- Implement `build_metadata(name, version, minimum_python, dependencies)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Return a fresh list rather than exposing caller-owned state.

## Run tests
`python -m pytest tests -q`
