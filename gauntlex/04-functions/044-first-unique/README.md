# firstunique

## Description
Implement `first_unique(text)` returning the first character that appears exactly once, or None if no such character exists. Case-sensitive.

## Requirements
- Implement the named function in `solution.py`.
- Return the value; do not print it.
- Do not add executable input handling at module import time.

## Examples
`firstunique("swiss")` → `"w"`

`firstunique("aabb")` → `None`

## Tips
Count all characters first, then scan the original order to find the first count of one.
