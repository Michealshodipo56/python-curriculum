# shortest_path

## Description
Given an undirected graph as a dictionary of node -> list of neighboring nodes, return the shortest path as a list from start to goal. Return [] if unreachable. When ties exist, follow neighbor-list order.

## Requirements
- Implement `shortest_path(graph, start, goal)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`shortest_path({"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}, "A", "D")` → `["A", "B", "D"]`

`shortest_path({"A": []}, "A", "Z")` → `[]`

## Tips
Breadth-first search visits nodes in increasing path length.
