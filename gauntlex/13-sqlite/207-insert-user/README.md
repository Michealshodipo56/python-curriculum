# insert_user

## Challenge
Insert a user into the existing users table with name and email; return the inserted integer row ID.

## Requirements
- Implement `insert_user(conn, name, email)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Use bound parameters and cursor.lastrowid.

## Run tests
`python -m pytest tests -q`
