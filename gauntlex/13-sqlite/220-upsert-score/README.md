# upsert_score

## Challenge
In scores(student TEXT PRIMARY KEY,score INTEGER), insert or update the score for a student, overwriting any previous value.

## Requirements
- Implement `upsert_score(conn, student, score)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
An UPSERT can update an existing primary key.

## Run tests
`python -m pytest tests -q`
