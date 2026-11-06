# Inherited Permissions

## Description
Roles can inherit permissions from parent roles. Collect all permissions granted directly or transitively through the hierarchy.

## Requirements
- Implement `effective_permissions(role_permissions, parents, assigned)` in `starter/solution.py`.
- Accept role-to-permissions mapping, role-to-parent-roles mapping, and assigned roles.
- Include permissions of every assigned role and all transitive ancestor roles.
- Assume the parent-role graph is acyclic.
- Return a sorted list of unique permission strings.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
Permissions flow through every ancestor role, not only direct parents. Multiple inheritance paths must not duplicate permissions.

## Tips
- Why can one role inherit permissions through several levels?

## Example Behavior
If `admin` inherits `editor` and `editor` grants `write`, an assigned `admin` role includes `write`.
