# top_customers

## Challenge
Return [user_id,total] for each user in orders(id,user_id,amount), ordered by total descending and user_id ascending; limit to nonnegative k.

## Requirements
- Implement `top_customers(conn, k)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Use GROUP BY, SUM, ORDER BY, and LIMIT.

## Run tests
`python -m pytest tests -q`
