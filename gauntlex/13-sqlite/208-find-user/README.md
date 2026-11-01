# Find One Record

## Description
Retrieve a user by its numeric identifier, handling the case where no row exists.

### Behavior contract
Return [id,name,email] for a user with the specified integer ID, or None if not found. Table users(id,name,email) exists.

## Requirements
- Implement `find_user(conn, user_id)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
A database row and a Python list are different representations of the same record.

Design the database interaction yourself; no SQL solution is provided.
