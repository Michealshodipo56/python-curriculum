# Guard the Balance

## Description

A bank account must protect its balance against invalid operations. Model deposits and withdrawals so the object remains consistent even when a transaction is rejected.

## Requirements

- Define `BankAccount(initial_balance=0)` in `starter/solution.py`.
- Expose the current amount through a `balance` property.
- Implement `deposit(amount)` and `withdraw(amount)` to change the balance.
- Raise `ValueError` for a negative initial balance or any nonpositive transaction amount.
- Raise `ValueError` when a withdrawal exceeds the available balance.
- Keep the balance unchanged when an operation fails.
- Use Python's standard library only and do not print or request input at import time.

## Tips

- Why should validation happen before changing the stored balance?
- Consider zero-value transactions and withdrawals exceeding the balance.

## Example Behavior

An account initialized with `10` has balance `15` after depositing `5`; withdrawing `20` raises `ValueError`.
