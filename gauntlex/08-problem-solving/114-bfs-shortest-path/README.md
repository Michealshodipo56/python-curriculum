# Shortest Route

## Description
Find a route with the fewest edges between two graph nodes. When multiple shortest routes exist, neighbor-list order determines the selected route.

## Requirements
- Implement `shortest_path(graph, start, goal)` in `starter/solution.py`.
- Accept a graph mapping nodes to lists of neighbors; interpret edges as specified by the adjacency lists.
- Return a list of nodes from `start` to `goal`, including both endpoints.
- Return `[]` when the goal is unreachable.
- Choose among equal-length paths by exploring neighbors in listed order.
- Do not mutate the graph.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does exploring paths by number of edges find a shortest route?
- How does neighbor order break ties?

## Example Behavior
`shortest_path({'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}, 'A', 'D')` → `['A', 'B', 'D']`.
