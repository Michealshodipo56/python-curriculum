# effective_permissions

## Challenge
Given mapping role->list of permissions, mapping role->list of parent roles, and a list of assigned roles, return sorted unique permissions inherited transitively. Assume the parent-role graph is acyclic.

## Requirements
- Implement `effective_permissions(role_permissions, parents, assigned)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Traverse role ancestry and collect permissions in a set.

## Run tests
`python -m pytest tests -q`
