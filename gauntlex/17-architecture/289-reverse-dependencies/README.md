# Who Depends on This?

## Description
A dependency graph points from packages to their requirements. Reverse those relationships to find the direct dependents of each package.

## Requirements
- Implement `reverse_dependencies(graph)` in `starter/solution.py`.
- Accept a mapping from package names to dependency-name lists.
- Include every name occurring as a key or dependency.
- Return a dictionary mapping each name to a sorted list of its direct dependents.
- Include empty lists for names with no dependents.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why should a dependency-only package still appear in the result?

## Example Behavior
`reverse_dependencies({'app': ['core'], 'tool': ['core']})` → `{'app': [], 'tool': [], 'core': ['app', 'tool']}`.
