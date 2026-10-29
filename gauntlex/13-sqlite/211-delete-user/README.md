# delete_user

## Challenge
Delete the user with the given integer ID. Return True if deleted and False if absent.

## Requirements
- Implement `delete_user(conn, user_id)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Use a bound DELETE query and inspect affected rows.

## Run tests
`python -m pytest tests -q`
