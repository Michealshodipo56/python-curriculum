# Store a JSON Document

## Description
Serialize a Python value into canonical JSON and save it as one database record.

### Behavior contract
Insert a compact, sorted-key JSON string representing value into documents(id INTEGER PRIMARY KEY,body TEXT). Return the inserted row ID.

## Requirements
- Implement `store_json(conn, value)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
Persist a stable text representation rather than a Python object's display string.

Implement the database behavior without using solution code from another task.
