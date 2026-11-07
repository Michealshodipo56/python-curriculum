# Change a User Email

## Description
Changing a stored email should affect only the intended user. Report whether the target record existed so callers can distinguish success from a missing ID.

## Requirements
- Implement `update_email(conn, user_id, email)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Update the email of the user identified by `user_id`.
- Assume `users(id,name,email)` exists.
- Return `True` if a row was updated and `False` if none matched.
- Keep all other user records unchanged.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips
- How can the number of affected rows tell you whether the user existed?
- Why should the identifier be parameterized?

## Example Behavior
`update_email(conn, 999, 'new@example.com')` → `False` when the user does not exist.
