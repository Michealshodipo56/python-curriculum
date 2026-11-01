# All or Nothing

## Description
Insert a group of users as one atomic operation, rolling back the entire group on any constraint failure.

### Behavior contract
Insert [name,email] pairs into users(id,name,email UNIQUE) atomically. If any insert violates a constraint, propagate sqlite3.IntegrityError and leave the table as it was before the call.

## Requirements
- Implement `insert_batch_atomic(conn, records)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
A batch must not leave earlier successful inserts behind when a later insert fails.

Implement the database behavior without using solution code from another task.
