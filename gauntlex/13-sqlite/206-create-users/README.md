# Define the Users Table

## Description

A reliable directory starts with a schema that prevents incomplete records and duplicate email addresses. Define the database constraints before any user records are inserted.

## Requirements

- Implement `create_users(conn)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Create the `users` table only if it does not already exist.
- Use `id INTEGER PRIMARY KEY`, `name TEXT NOT NULL`, and `email TEXT NOT NULL UNIQUE`.
- Do not remove or overwrite an existing table.
- Use the supplied SQLite connection.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips

- Which integrity rules belong in the database rather than only in application code?
- What should a second call do when the table already exists?

## Example Behavior

Calling `create_users(conn)` twice leaves one usable table with the required constraints.
