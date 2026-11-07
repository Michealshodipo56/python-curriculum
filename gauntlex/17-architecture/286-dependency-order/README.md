# Build in Dependency Order

## Description
A build system must complete prerequisites before their dependents. Produce a deterministic sequence even when several tasks are ready simultaneously.

## Requirements
- Implement `dependency_order(graph)` in `starter/solution.py`.
- Accept a mapping of task names to prerequisite-name lists.
- Include tasks mentioned only as prerequisites.
- Return a topological ordering with every prerequisite before its dependent.
- When several tasks are ready, choose the lexicographically smallest available name.
- Raise `ValueError` if any cycle makes completion impossible.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A task mentioned only as a prerequisite must still appear in the final order; disconnected tasks also belong in the result.

## Tips
- Why does choosing among ready tasks require a consistent rule?

## Example Behavior
For `{'app': ['lib'], 'lib': []}`, return `['lib', 'app']`.
