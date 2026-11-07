# Permission by Role

## Description

Role-based access control grants actions through assigned roles. Determine whether any known role explicitly authorizes a requested permission.

## Requirements

- Implement `has_permission(role_permissions, user_roles, permission)` in `starter/solution.py`.
- Accept a mapping from roles to permission lists, assigned user roles, and a requested permission.
- Return `True` if at least one assigned role includes that permission.
- Treat unknown roles as granting nothing.
- Return `False` when no assigned role grants the permission.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

Permission checks use direct grants from assigned roles only. Unknown roles grant nothing, and a missing permission is denied.

## Tips

- Why must an unknown role never grant permissions by default?

## Example Behavior

`has_permission({'editor': ['write']}, ['editor'], 'write')` → `True`.
