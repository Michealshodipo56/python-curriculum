# Shape Invariants

## Description
An object representing a rectangle should begin in a valid state. Require valid dimensions during construction so subsequent calculations can rely on them.

## Requirements
- Define `Rectangle(width, height)` in `starter/solution.py`.
- Accept positive numeric width and height values.
- Raise `ValueError` if either dimension is zero or negative.
- Implement `area()` to return the rectangle's area.
- Implement `perimeter()` to return the total boundary length.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- Which rules belong in object construction?
- How does enforcing valid dimensions simplify later calculations?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
For `Rectangle(4, 3)`, `area()` returns `12` and `perimeter()` returns `14`.
