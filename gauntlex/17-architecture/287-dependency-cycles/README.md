# Find Dependency Loops

## Description
Circular prerequisites prevent any valid build order. Detect a cycle even when some nodes appear only in other tasks' dependency lists.

## Requirements
- Implement `has_dependency_cycle(graph)` in `starter/solution.py`.
- Accept a directed mapping of tasks to prerequisites.
- Return `True` if any directed cycle exists; otherwise `False`.
- Include names appearing only as prerequisites.
- Do not change the graph.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why is revisiting a fully explored node different from revisiting an active path?

## Example Behavior
`has_dependency_cycle({'a': ['b'], 'b': ['a']})` → `True`.
