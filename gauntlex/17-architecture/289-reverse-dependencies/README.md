# Who Depends on This?

## Description
Reverse a dependency graph so each component lists its direct dependents.

### Behavior contract
Given a mapping of package to list of dependencies, return a dictionary mapping every package or dependency name to a sorted list of packages that depend directly on it.

## Requirements
- Implement `reverse_dependencies(graph)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Include components that appear only as dependencies.

Design your own implementation from the specified behavior.
