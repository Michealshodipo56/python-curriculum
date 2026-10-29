# inventory

## Description
Implement Inventory with stock(name,quantity), sell(name,quantity), and quantity(name). Stock and sell quantities must be positive integers; selling more than available raises ValueError. Missing items have quantity zero.

## Requirements
- Define `Inventory` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Examples
The tests exercise the class methods and expected state changes.

## Tips
Use a dictionary keyed by item name and validate transactions before updating.
