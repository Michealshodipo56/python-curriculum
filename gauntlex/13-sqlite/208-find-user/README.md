# find_user

## Challenge
Return [id,name,email] for a user with the specified integer ID, or None if not found. Table users(id,name,email) exists.

## Requirements
- Implement `find_user(conn, user_id)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Fetch one parameterized row and convert it to a list.

## Run tests
`python -m pytest tests -q`
