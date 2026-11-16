# Build in Parallel Layers

## Description

Implement `service_layers(graph)` in `starter/solution.py`. Include names that occur only as prerequisites.

## Requirements

- Implement `service_layers(graph)` in `starter/solution.py`.
- Accept a mapping of services to prerequisite-name lists.
- Include names that occur only as prerequisites.
- Return successive layers, each a sorted list of all services ready at that stage.
- Place each service after every prerequisite.
- Raise `ValueError` if a dependency cycle exists.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

Independent services are grouped in the same layer; a service may enter only after all its prerequisites are in earlier layers.

## Tips

- **Concept to understand:** Independent services can be built in parallel once all their prerequisites are complete. Group services by the earliest layer in which they become ready.
- Why should all currently ready services share a layer?

## Example Behavior

`service_layers({'app': ['db', 'api'], 'api': []})` → `[['api', 'db'], ['app']]`.
