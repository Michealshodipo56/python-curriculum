# order_total

## Challenge
Return total amount for a given user_id in orders(id,user_id,amount). Return 0 if there are no matching orders.

## Requirements
- Implement `order_total(conn, user_id)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
COALESCE can replace a NULL aggregate with zero.

## Run tests
`python -m pytest tests -q`
