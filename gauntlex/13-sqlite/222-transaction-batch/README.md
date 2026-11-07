# All or Nothing

## Description

Import multiple users as one unit of work. If any record violates a database constraint, none of the records from that batch may remain.

## Requirements

- Implement `insert_batch_atomic(conn, records)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Insert each `[name,email]` pair into `users(id,name,email UNIQUE)`.
- Treat the batch atomically, including when an error occurs partway through.
- Propagate `sqlite3.IntegrityError` on a constraint violation.
- On failure, restore the table to its pre-call contents.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips

- Why is a sequence of independent inserts insufficient?
- What should happen to earlier successful inserts when a later one fails?

## Example Behavior

If the third record repeats an existing unique email, the first two inserts from that batch must also be undone.
