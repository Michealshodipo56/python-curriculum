# Build in Parallel Layers

## Description
Group services into successive layers whose prerequisites have already been completed.

### Behavior contract
Given a dependency graph mapping service to prerequisite services, return successive sorted layers of services that can be built together. Include dependency-only nodes. Raise ValueError on cycles.

## Requirements
- Implement `service_layers(graph)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
All currently ready services can belong to the same layer.

Design your own implementation from the specified behavior.
