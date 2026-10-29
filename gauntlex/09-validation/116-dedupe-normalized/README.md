# dedupe_normalized

## Description
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
Normalize before comparing, and preserve the first occurrence order.
