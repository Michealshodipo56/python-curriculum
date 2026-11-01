# Find Dependency Loops

## Description
Detect whether a prerequisite graph contains an impossible circular dependency.

### Behavior contract
Return True if the directed prerequisite graph contains a cycle. Include names that appear only in prerequisite lists.

## Requirements
- Implement `has_dependency_cycle(graph)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Revisiting a fully explored node is different from encountering a node still on the active path.

Design your own implementation from the specified behavior.
