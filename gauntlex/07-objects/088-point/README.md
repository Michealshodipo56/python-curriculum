# Immutable Coordinates

## Description
Represent a point that cannot be changed after creation, and calculate distances between points.

### Behavior contract
Implement immutable Point(x,y) with distance_to(other) returning Euclidean distance. Attempting to assign x or y after construction must fail.

## Requirements
- Define `Point` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
How can a class guarantee that an object's coordinates remain stable?

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
