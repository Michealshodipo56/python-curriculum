# events_on_or_after

## Challenge
Return [id,event_date] rows from events(id,event_date TEXT) where event_date >= ISO date string cutoff, ordered by event_date then id. Dates are valid YYYY-MM-DD.

## Requirements
- Implement `events_on_or_after(conn, cutoff)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
Canonical ISO dates sort lexicographically.

## Run tests
`python -m pytest tests -q`
