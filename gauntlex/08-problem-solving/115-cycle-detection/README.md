# Detect a Loop

## Description
Determine whether following directed graph edges can lead back to an active path.

### Behavior contract
Return whether a directed graph represented as node -> list of outgoing neighbors contains a cycle. Neighbor nodes may be absent as dictionary keys.

## Requirements
- Implement `has_cycle(graph)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`has_cycle({"a": ["b"], "b": ["c"], "c": ["a"]})` → `True`

`has_cycle({"a": ["b"], "b": []})` → `False`

## Tips
A node visited in an earlier completed branch is not necessarily evidence of a cycle.

The examples define expected behavior; design your own implementation.
