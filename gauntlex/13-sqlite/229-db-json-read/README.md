# load_json

## Challenge
Read body from documents(id,body TEXT) for the given ID, parse as JSON, and return the resulting value. Return None if no row exists.

## Requirements
- Implement `load_json(conn, doc_id)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Use a parameterized SELECT and decode JSON only if a row exists.

## Run tests
`python -m pytest tests -q`
