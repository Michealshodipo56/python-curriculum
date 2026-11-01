# Ensure an Index

## Description
Add a named index for email lookup in a way that remains safe to repeat.

### Behavior contract
Create an index named idx_users_email on users(email) if absent. Repeated calls must not fail.

## Requirements
- Implement `ensure_email_index(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
Schema setup should not fail merely because it has already been performed.

Implement the database behavior without using solution code from another task.
