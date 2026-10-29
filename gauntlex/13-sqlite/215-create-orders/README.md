# create_orders

## Challenge
Create orders(id INTEGER PRIMARY KEY,user_id INTEGER NOT NULL,amount INTEGER NOT NULL CHECK(amount>=0)) if it does not exist.

## Requirements
- Implement `create_orders(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Define nonnegative amounts using a CHECK constraint.

## Run tests
`python -m pytest tests -q`
