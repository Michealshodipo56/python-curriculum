# Find One Record

## Description

A user ID identifies at most one directory entry. Retrieve that record in a predictable Python representation, or clearly indicate that it does not exist.

## Requirements

- Implement `find_user(conn, user_id)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Assume the `users(id,name,email)` table exists.
- Find the row with the supplied integer `user_id`.
- Return `[id, name, email]` when found, or `None` otherwise.
- Do not change any database rows.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips

- Why is a missing record different from a record with an empty field?
- How should a SQLite row be represented in the return value?

## Example Behavior

`find_user(conn, 999)` → `None` when no row has that ID.
