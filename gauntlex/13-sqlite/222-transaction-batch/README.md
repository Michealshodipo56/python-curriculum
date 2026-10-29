# insert_batch_atomic

## Challenge
Insert [name,email] pairs into users(id,name,email UNIQUE) atomically. If any insert violates a constraint, propagate sqlite3.IntegrityError and leave the table as it was before the call.

## Requirements
- Implement `insert_batch_atomic(conn, records)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Hints
A SAVEPOINT supports rollback even when the caller already has an active transaction.

## Run tests
`python -m pytest tests -q`
