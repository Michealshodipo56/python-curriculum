# create_users

## Challenge
Create a users table if absent, with id INTEGER PRIMARY KEY, name TEXT NOT NULL, and email TEXT NOT NULL UNIQUE.

## Requirements
- Implement `create_users(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Use CREATE TABLE IF NOT EXISTS.

## Run tests
`python -m pytest tests -q`
