# Allowlisted Sorting

## Description
Support caller-selected sorting without allowing arbitrary SQL identifiers or directions.

### Behavior contract
Return [id,name] rows from users(id,name,email), ordered by a caller-specified field `id` or `name`, and direction `asc` or `desc` (case-insensitive). Raise ValueError for unsupported fields or directions.

## Requirements
- Implement `sorted_users(conn, field, direction)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
SQL parameters protect values, but column names need an explicit allowlist.

Implement the database behavior without using solution code from another task.
