# Stock Ledger

## Description

An inventory tracks how many units of each product are available. Model stock additions and sales without permitting impossible transactions.

## Requirements

- Define `Inventory` in `starter/solution.py`.
- Implement `stock(name, quantity)` to increase a product's quantity.
- Implement `sell(name, quantity)` to decrease the available quantity.
- Require positive integer quantities for both operations.
- Raise `ValueError` for invalid quantities or sales exceeding available stock.
- Implement `quantity(name)` and return `0` for unknown products.
- Use Python's standard library only and do not print or request input at import time.

## Tips

- What state must remain unchanged after a failed sale?
- How should a product with no prior stock be treated?

## Example Behavior

After stocking `'pen'` with `5` units and selling `2`, `quantity('pen')` returns `3`.
