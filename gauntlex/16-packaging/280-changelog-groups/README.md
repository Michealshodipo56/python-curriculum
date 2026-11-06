# Organize Changes

## Description
Release changes can be grouped by category for easier reading without changing the order in which changes were supplied.

## Requirements
- Implement `group_changes(entries)` in `starter/solution.py`.
- Accept `[category, description]` pairs.
- Return a dictionary mapping each category to its list of descriptions.
- Preserve original description order within each category.
- Do not discard earlier descriptions when a category repeats.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why does assigning a new list for every repeated category lose information?

## Example Behavior
`group_changes([['fix', 'A'], ['feat', 'B'], ['fix', 'C']])` → `{'fix': ['A', 'C'], 'feat': ['B']}`.
