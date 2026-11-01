# Guard the Balance

## Description
Manage account state through operations that enforce financial rules.

### Behavior contract
Implement BankAccount(initial_balance=0) with deposit(amount), withdraw(amount), and balance property. Negative initial balances or nonpositive transactions raise ValueError; withdrawing more than the balance raises ValueError.

## Requirements
- Define `BankAccount` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
Validate a transaction before changing the balance; what state should remain after an error?

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
