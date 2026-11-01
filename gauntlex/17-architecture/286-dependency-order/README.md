# Build in Dependency Order

## Description
Find a valid order for completing tasks whose prerequisites form a directed graph.

### Behavior contract
Given a dictionary mapping task names to prerequisite-name lists, return a valid topological order including prerequisite-only names. When multiple nodes are available, choose the lexicographically smallest. Raise ValueError for a cycle.

## Requirements
- Implement `dependency_order(graph)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
If several tasks are ready, the tie-breaking rule must still produce deterministic order.

Design your own implementation from the specified behavior.
