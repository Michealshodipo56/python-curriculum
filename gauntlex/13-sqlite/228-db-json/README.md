# store_json

## Challenge
Insert a compact, sorted-key JSON string representing value into documents(id INTEGER PRIMARY KEY,body TEXT). Return the inserted row ID.

## Requirements
- Implement `store_json(conn, value)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Serialize the value before binding it into an INSERT.

## Run tests
`python -m pytest tests -q`
