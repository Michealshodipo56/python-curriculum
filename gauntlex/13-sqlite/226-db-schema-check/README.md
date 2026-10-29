# table_exists

## Challenge
Return True if a table with the given name exists in sqlite_schema; otherwise False. Ignore views and indexes.

## Requirements
- Implement `table_exists(conn, table_name)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Query sqlite_schema with a parameterized name and type='table'.

## Run tests
`python -m pytest tests -q`
