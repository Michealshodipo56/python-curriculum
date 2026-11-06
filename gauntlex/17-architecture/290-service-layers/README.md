# Build in Parallel Layers

## Description
Independent services can be built in parallel once all their prerequisites are complete. Group services by the earliest layer in which they become ready.

## Requirements
- Implement `service_layers(graph)` in `starter/solution.py`.
- Accept a mapping of services to prerequisite-name lists.
- Include names that occur only as prerequisites.
- Return successive layers, each a sorted list of all services ready at that stage.
- Place each service after every prerequisite.
- Raise `ValueError` if a dependency cycle exists.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why should all currently ready services share a layer?

## Example Behavior
`service_layers({'app': ['db', 'api'], 'api': []})` → `[['api', 'db'], ['app']]`.
