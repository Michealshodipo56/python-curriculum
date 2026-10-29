# users_page

## Challenge
Return [id,name] rows from users(id,name,email) ordered by id ascending for 1-based page and positive page_size. Raise ValueError for invalid page or page_size.

## Requirements
- Implement `users_page(conn, page, page_size)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Use LIMIT and OFFSET as bound integers.

## Run tests
`python -m pytest tests -q`
