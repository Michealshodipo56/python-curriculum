# Remove a User

## Description

Delete a specific directory entry without disturbing other users, and report whether the target was actually present.

## Requirements

- Implement `delete_user(conn, user_id)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Delete only the row with the supplied integer ID.
- Return `True` when a row was deleted, `False` if none matched.
- Leave unrelated records untouched.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips

- How can the affected-row count distinguish a missing user from a successful deletion?

## Example Behavior

Deleting a missing user returns `False`; deleting an existing user returns `True`.
