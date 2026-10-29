# has_cycle

## Description
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
Track nodes currently on the depth-first recursion path separately from fully explored nodes.
