# Weighted Shortest Paths

## Description
Determine the least total cost from a starting node to every reachable node in a directed weighted graph. A path discovered first is not necessarily the cheapest.

## Requirements
- Implement `dijkstra_distances(graph, start)` in `starter/solution.py`.
- `graph` maps hashable nodes to lists of `[neighbor, weight]` edges; all valid weights are nonnegative.
- Return a mapping from each reachable node to its minimum total distance, including `start: 0`.
- Include reachable nodes that appear only as neighbors, not as graph keys.
- Raise `ValueError` if a negative edge weight is supplied.
- Do not mutate the graph or print.
- Use Python's standard library only.

## Tips
- Why can a later route improve an earlier tentative distance?
- What should happen to a reachable neighbor absent from the graph's keys?

## Example Behavior
`dijkstra_distances({'A': [['B', 5], ['C', 1]], 'C': [['B', 2]]}, 'A')` → `{'A': 0, 'C': 1, 'B': 3}`.
