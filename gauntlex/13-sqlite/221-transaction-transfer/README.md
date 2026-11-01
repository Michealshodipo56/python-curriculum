# Atomic Account Transfer

## Description
Move money between two account balances without ever leaving a partial transfer.

### Behavior contract
Move a positive integer amount between account IDs in accounts(id INTEGER PRIMARY KEY,balance INTEGER NOT NULL). Raise ValueError if amount <=0, either account is absent, or the source lacks funds. Failed transfers must leave both balances unchanged.

## Requirements
- Implement `transfer(conn, source_id, target_id, amount)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
A failed transfer must preserve both balances, even if one update has already been attempted.

Implement the database behavior without using solution code from another task.
