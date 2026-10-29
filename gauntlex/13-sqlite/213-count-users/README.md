# count_users

## Challenge
Return the number of rows in users(id,name,email).

## Requirements
- Implement `count_users(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
COUNT(*) returns a single aggregate row.

## Run tests
`python -m pytest tests -q`
