# Count the Directory

## Description
Report how many user records exist without retrieving every record.

### Behavior contract
Return the number of rows in users(id,name,email).

## Requirements
- Implement `count_users(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
An aggregate query can return one value representing many rows.

Design the database interaction yourself; no SQL solution is provided.
