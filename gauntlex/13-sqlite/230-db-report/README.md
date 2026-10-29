# revenue_report

## Challenge
Return [category,total] rows for sales(id,category,amount INTEGER), sorted by total descending then category ascending. Sum all amounts per category; return [] for empty table.

## Requirements
- Implement `revenue_report(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Aggregate in SQL rather than fetching all rows into Python.

## Run tests
`python -m pytest tests -q`
