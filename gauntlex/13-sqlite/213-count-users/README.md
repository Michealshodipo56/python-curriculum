# Count the Directory

## Description

A directory count should return one number, without loading every user record into Python.

## Requirements

- Implement `count_users(conn)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Return the number of rows in `users(id,name,email)` as an integer.
- Return `0` for an empty table.
- Do not change database contents.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips

- What does a SQL aggregate return when no records exist?

## Example Behavior

An empty directory returns `0`; inserting one user makes the result `1`.
