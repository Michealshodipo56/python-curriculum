# has_permission

## Challenge
Given mapping role->list of permission strings, a list of user roles, and a permission, return True if any assigned role grants it. Unknown roles grant nothing.

## Requirements
- Implement `has_permission(role_permissions, user_roles, permission)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Use an explicit allowlist rather than inferring permissions from role names.

## Run tests
`python -m pytest tests -q`
