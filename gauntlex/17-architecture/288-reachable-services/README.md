# reachable_services

## Challenge
Given a mapping of service to list of downstream services and a starting service, return sorted reachable service names including the start, even if it is not a key.

## Requirements
- Implement `reachable_services(graph, start)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Track visited nodes to handle cycles.

## Run tests
`python -m pytest tests -q`
