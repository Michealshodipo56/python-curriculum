# Route Specificity

## Description

Routes with more fixed path segments are more specific than routes dominated by placeholders. Calculate a simple specificity score.

## Requirements

- Implement `route_priority(template)` in `starter/solution.py`.
- Split the template into path segments, ignoring empty segments from leading or trailing slashes.
- Count each literal segment as one point.
- Treat a segment as dynamic only when it starts with `{` and ends with `}`.
- Return the integer literal-segment count.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

Count only complete fixed segments. A segment beginning with `{` and ending with `}` is dynamic even when its contents are unusual.

## Tips

- Why is a placeholder less specific than a fixed path segment?

## Example Behavior

`route_priority('/users/{id}/posts')` → `2`.
