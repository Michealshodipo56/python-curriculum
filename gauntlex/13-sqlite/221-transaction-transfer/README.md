# transfer

## Challenge
Move a positive integer amount between account IDs in accounts(id INTEGER PRIMARY KEY,balance INTEGER NOT NULL). Raise ValueError if amount <=0, either account is absent, or the source lacks funds. Failed transfers must leave both balances unchanged.

## Requirements
- Implement `transfer(conn, source_id, target_id, amount)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
A savepoint can make multiple writes atomic without assuming connection transaction state.

## Run tests
`python -m pytest tests -q`
