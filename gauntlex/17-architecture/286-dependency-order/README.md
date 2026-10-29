# dependency_order

## Challenge
Given a dictionary mapping task names to prerequisite-name lists, return a valid topological order including prerequisite-only names. When multiple nodes are available, choose the lexicographically smallest. Raise ValueError for a cycle.

## Requirements
- Implement `dependency_order(graph)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Track indegrees and use a priority queue for deterministic choices.

## Run tests
`python -m pytest tests -q`
