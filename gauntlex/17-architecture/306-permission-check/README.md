# Permission by Role

## Description
Determine whether any assigned role explicitly grants a requested permission.

### Behavior contract
Given mapping role->list of permission strings, a list of user roles, and a permission, return True if any assigned role grants it. Unknown roles grant nothing.

## Requirements
- Implement `has_permission(role_permissions, user_roles, permission)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Unknown roles must grant nothing.

Design your own implementation from the specified behavior.
