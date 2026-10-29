# group_counts

## Challenge
Return [category,count] for rows in events(id,category), ordered by count descending then category ascending.

## Requirements
- Implement `group_counts(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
GROUP BY and a secondary sort key make ties predictable.

## Run tests
`python -m pytest tests -q`
