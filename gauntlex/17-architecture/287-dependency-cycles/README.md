# has_dependency_cycle

## Challenge
Return True if the directed prerequisite graph contains a cycle. Include names that appear only in prerequisite lists.

## Requirements
- Implement `has_dependency_cycle(graph)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Three-color depth-first search distinguishes active from completed nodes.

## Run tests
`python -m pytest tests -q`
