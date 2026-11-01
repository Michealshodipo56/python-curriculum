# Route Specificity

## Description
Score route templates according to how many literal segments they contain.

### Behavior contract
Return the number of literal segments in a route template. A segment is dynamic only if it starts with { and ends with }. Ignore empty segments caused by leading or trailing slashes.

## Requirements
- Implement `route_priority(template)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Dynamic segments are less specific than literal ones.

Design your own implementation from the specified behavior.
