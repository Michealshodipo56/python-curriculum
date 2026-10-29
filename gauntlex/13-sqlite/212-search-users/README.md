# search_users

## Challenge
Return [id,name] rows from users(id,name,email) whose name contains the supplied substring case-insensitively, ordered by id. Treat % and _ as literal characters, not SQL wildcards.

## Requirements
- Implement `search_users(conn, term)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
LIKE requires escaping its wildcard characters when searching literal text.

## Run tests
`python -m pytest tests -q`
