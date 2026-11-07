# Read the User Directory

## Description

Database queries do not guarantee insertion order. Retrieve the complete user directory in a stable order suitable for display or further processing.

## Requirements

- Implement `list_users(conn)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Read all rows from `users(id,name,email)`.
- Return a list of `[id, name, email]` records.
- Order records by ascending ID.
- Return `[]` when the table is empty.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips

- Why should sorting be requested explicitly?
- What is the expected result for an empty directory?

## Example Behavior

An empty `users` table produces `[]`; populated results are ordered by ID.
