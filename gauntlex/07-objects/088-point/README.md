# Immutable Coordinates

## Description

A point identifies a fixed location in two-dimensional space. Create a class whose coordinates cannot be reassigned after construction and that can measure distance to another point.

## Requirements

- Define `Point(x, y)` in `starter/solution.py`.
- Store the point's `x` and `y` coordinates.
- Prevent assignments that change either coordinate after construction.
- Implement `distance_to(other)` to return the Euclidean distance to another point.
- Keep the original point unchanged during distance calculations.
- Use Python's standard library only and do not print or request input at import time.

## Tips

- What distinguishes an immutable object from an ordinary mutable one?
- How can horizontal and vertical differences determine distance?

## Example Behavior

The distance from `Point(0, 0)` to `Point(3, 4)` is `5`; assigning a new `x` afterward must fail.
