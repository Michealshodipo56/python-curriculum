# Remove a User

## Description
Delete one identified user and report whether the record existed.

### Behavior contract
Delete the user with the given integer ID. Return True if deleted and False if absent.

## Requirements
- Implement `delete_user(conn, user_id)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
Deleting a nonexistent row should not be confused with deleting an existing one.

Design the database interaction yourself; no SQL solution is provided.
