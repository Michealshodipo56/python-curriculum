# list_users

## Challenge
Return a list of [id,name,email] rows from users(id,name,email), ordered by id ascending.

## Requirements
- Implement `list_users(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Use ORDER BY id for deterministic results.

## Run tests
`python -m pytest tests -q`
