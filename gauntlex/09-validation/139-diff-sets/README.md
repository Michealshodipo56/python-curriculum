# set_diff

## Description
Return a dictionary with keys `added`, `removed`, and `shared`, each containing a sorted list of strings comparing old and new collections. Ignore duplicates.

## Requirements
- Implement `set_diff(old, new)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`set_diff(["a", "b"], ["b", "c"])` → `{"added": ["c"], "removed": ["a"], "shared": ["b"]}`

`set_diff([], [])` → `{"added": [], "removed": [], "shared": []}`

## Tips
Use set differences and intersection.
