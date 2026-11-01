# Distinct After Normalization

## Description
Clean a collection of strings and keep only the first occurrence of each meaningful normalized value.

### Behavior contract
Return unique trimmed, casefolded nonempty strings in their first appearance order.

## Requirements
- Implement `dedupe_normalized(items)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`dedupe_normalized(["  Ada ", "ada", "BOB", "bob", "  "])` → `["ada", "bob"]`

`dedupe_normalized([])` → `[]`

## Tips
Normalization must happen before checking for duplicates. Consider empty strings and mixed case.

The examples show required behavior, not an implementation.
