# Stock Ledger

## Description
Maintain item quantities while preventing invalid or impossible stock transactions.

### Behavior contract
Implement Inventory with stock(name,quantity), sell(name,quantity), and quantity(name). Stock and sell quantities must be positive integers; selling more than available raises ValueError. Missing items have quantity zero.

## Requirements
- Define `Inventory` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
How should the object respond when a sale exceeds the quantity on hand?

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
