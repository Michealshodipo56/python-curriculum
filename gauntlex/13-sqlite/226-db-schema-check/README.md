# Inspect the Schema

## Description
Determine whether a named database table exists without confusing it with views or indexes.

### Behavior contract
Return True if a table with the given name exists in sqlite_schema; otherwise False. Ignore views and indexes.

## Requirements
- Implement `table_exists(conn, table_name)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
The schema records different object types; table existence is more specific than name existence.

Implement the database behavior without using solution code from another task.
