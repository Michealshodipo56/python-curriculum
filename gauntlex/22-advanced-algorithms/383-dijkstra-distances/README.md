# Weighted Shortest Paths

## Description
Compute minimum distances from one graph node to all reachable nodes with nonnegative edge weights.

### Behavior contract
Given mapping node->list of [neighbor,nonnegative_weight] edges and a start node, return shortest distance to every reachable node (including start=0). Nodes are hashable. Include neighbor-only nodes; reject negative weights with ValueError.

## Requirements
- Implement `dijkstra_distances(graph, start)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Tips
A previously discovered route may be improved by a later, cheaper path.

The task is to design an implementation that meets both behavior and efficiency requirements.
