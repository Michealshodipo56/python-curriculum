# update_email

## Challenge
Update the email of a user by integer ID. Return True if a row was updated, otherwise False. Table users(id,name,email) exists.

## Requirements
- Implement `update_email(conn, user_id, email)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Check cursor.rowcount after a parameterized UPDATE.

## Run tests
`python -m pytest tests -q`
