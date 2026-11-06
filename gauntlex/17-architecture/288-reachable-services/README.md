# Downstream Reachability

## Description
A service dependency graph can show which components may be reached from one starting point. Explore transitively without looping forever.

## Requirements
- Implement `reachable_services(graph, start)` in `starter/solution.py`.
- Accept a mapping from service names to lists of downstream services and a start name.
- Include the start itself, even if it is not a graph key.
- Return every reachable service name once, sorted alphabetically.
- Handle cycles without infinite traversal.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why must visited services be tracked?

## Example Behavior
`reachable_services({'a': ['b'], 'b': ['c']}, 'a')` → `['a', 'b', 'c']`.
