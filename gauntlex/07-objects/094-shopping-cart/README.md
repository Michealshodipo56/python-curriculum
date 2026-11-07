# Cart Rules

## Description

Maintain products, prices, and quantities in a shopping cart without accepting contradictory entries.

## Requirements

- Implement `ShoppingCart` in `starter/solution.py`.
- Provide `add(name, price, quantity=1)` with nonnegative prices and positive integer quantities.
- Increase quantity when an existing name is added at the same price.
- Raise `ValueError` if an existing name is added with a different price.
- Provide `remove(name)` to delete the entire item; raise `KeyError` if missing.
- Provide `total()` to calculate the sum of price times quantity.
- Use the Python standard library only. Do not print or request input at import time.

## Tips

- Why should an existing product not silently change its price?
- What should happen to a cart's total after removal?

## Example Behavior

Adding two items at price `3` and one more at the same price produces a total of `9`.
