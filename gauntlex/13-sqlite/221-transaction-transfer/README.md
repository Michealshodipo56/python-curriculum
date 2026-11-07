# Atomic Account Transfer

## Description
A transfer changes two balances that must stay consistent. Treat the debit and credit as one indivisible operation.

## Requirements
- Implement `transfer(conn, source_id, target_id, amount)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `accounts(id INTEGER PRIMARY KEY,balance INTEGER NOT NULL)` exists.
- Transfer a positive integer amount from source to target.
- Raise `ValueError` if the amount is nonpositive, either account is absent, or the source has insufficient funds.
- On failure, leave both balances exactly as they were before the call.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why must a debit and credit succeed or fail together?
- What should happen if validation fails after a tentative change?

## Example Behavior
An invalid transfer raises `ValueError` and leaves both account balances unchanged.
