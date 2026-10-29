# service_layers

## Challenge
Given a dependency graph mapping service to prerequisite services, return successive sorted layers of services that can be built together. Include dependency-only nodes. Raise ValueError on cycles.

## Requirements
- Implement `service_layers(graph)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Remove all currently ready nodes as one layer before discovering the next.

## Run tests
`python -m pytest tests -q`
