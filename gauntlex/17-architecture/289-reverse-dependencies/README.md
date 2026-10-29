# reverse_dependencies

## Challenge
Given a mapping of package to list of dependencies, return a dictionary mapping every package or dependency name to a sorted list of packages that depend directly on it.

## Requirements
- Implement `reverse_dependencies(graph)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Initialize all known nodes, then invert each directed edge.

## Run tests
`python -m pytest tests -q`
