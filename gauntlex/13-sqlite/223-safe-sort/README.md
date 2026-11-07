# Allowlisted Sorting

## Description
Caller-selected sorting can be dangerous when SQL identifiers are constructed from untrusted input. Permit only known columns and directions.

## Requirements
- Implement `sorted_users(conn, field, direction)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Accept a sort field of `id` or `name`.
- Accept `asc` or `desc` without regard to case.
- Raise `ValueError` for unsupported fields or directions.
- Return `[id, name]` rows sorted as requested from `users(id,name,email)`.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why do SQL value parameters not safely substitute for column identifiers?
- What role does an explicit allowlist play?

## Example Behavior
`sorted_users(conn, 'name', 'DESC')` returns `[id, name]` rows ordered by descending name.
