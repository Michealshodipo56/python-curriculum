# Search Names Literally

## Description
Find users whose names contain a supplied term, without allowing SQL wildcard characters to change its meaning.

### Behavior contract
Return [id,name] rows from users(id,name,email) whose name contains the supplied substring case-insensitively, ordered by id. Treat % and _ as literal characters, not SQL wildcards.

## Requirements
- Implement `search_users(conn, term)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
A percent sign entered by a user should be searched as text, not interpreted as a pattern.

Design the database interaction yourself; no SQL solution is provided.
