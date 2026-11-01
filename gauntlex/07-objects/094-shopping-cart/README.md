# Cart Rules

## Description
Maintain products, prices, and quantities without allowing contradictory entries.

### Behavior contract
Implement ShoppingCart with add(name,price,quantity=1), remove(name), and total(). Price must be nonnegative and quantity a positive integer. Adding an existing name with a different price raises ValueError. remove deletes the entire named item and raises KeyError if missing.

## Requirements
- Define `ShoppingCart` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
What should happen when an existing item is added again at a different price?

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
