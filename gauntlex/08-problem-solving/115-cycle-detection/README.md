# Detect a Loop

## Description
A directed graph contains a cycle if a path of outgoing edges can return to a node already on that same active path.

## Requirements
- Implement `has_cycle(graph)` in `starter/solution.py`.
- Accept a dictionary mapping nodes to lists of outgoing neighbors.
- Return `True` if any directed cycle exists and `False` otherwise.
- Treat neighbor nodes absent from the dictionary as nodes with no outgoing edges.
- Do not mutate the graph.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why is visiting a node from an earlier completed branch not enough to prove a cycle?
- How does a self-loop differ from a dead end?

## Example Behavior
`has_cycle({'a': ['b'], 'b': ['c'], 'c': ['a']})` → `True`; `has_cycle({'a': ['b'], 'b': []})` → `False`.
