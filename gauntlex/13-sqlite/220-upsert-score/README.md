# Create or Replace a Score

## Description
Maintain one score per student by inserting new records or updating existing ones.

### Behavior contract
In scores(student TEXT PRIMARY KEY,score INTEGER), insert or update the score for a student, overwriting any previous value.

## Requirements
- Implement `upsert_score(conn, student, score)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
The primary key determines whether the operation creates a row or changes one.

Implement the database behavior without using solution code from another task.
