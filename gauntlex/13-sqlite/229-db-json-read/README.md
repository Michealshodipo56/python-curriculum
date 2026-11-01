# Load a JSON Document

## Description
Retrieve a saved JSON record and restore its structured Python value.

### Behavior contract
Read body from documents(id,body TEXT) for the given ID, parse as JSON, and return the resulting value. Return None if no row exists.

## Requirements
- Implement `load_json(conn, doc_id)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
A missing database row and a stored JSON null may both lead to `None`, but for different reasons.

Implement the database behavior without using solution code from another task.
