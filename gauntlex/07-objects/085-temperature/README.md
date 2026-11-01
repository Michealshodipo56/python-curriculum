# Two Scales, One Value

## Description
Represent a temperature with one underlying value and expose another scale as a derived property.

### Behavior contract
Implement Temperature(celsius) with celsius and fahrenheit read-only properties, and from_fahrenheit(cls, value) classmethod returning a Temperature.

## Requirements
- Define `Temperature` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
A conversion should not require keeping two independently mutable values.

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
