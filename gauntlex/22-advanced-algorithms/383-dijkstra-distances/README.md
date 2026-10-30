# dijkstra_distances

## Challenge
Given mapping node->list of [neighbor,nonnegative_weight] edges and a start node, return shortest distance to every reachable node (including start=0). Nodes are hashable. Include neighbor-only nodes; reject negative weights with ValueError.

## Requirements
- Implement `dijkstra_distances(graph, start)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Hint
Use a priority queue and ignore stale distance entries.

## Run tests
`python -m pytest tests -q`
