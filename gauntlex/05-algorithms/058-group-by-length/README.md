# group_by_length

## Description
Return a dictionary mapping each word length to the list of words of that length, preserving input order within each list.

## Requirements
- Implement `group_by_length(words)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`group_by_length(["a", "cat", "be", "dog"])` → `{1: ["a"], 2: ["be"], 3: ["cat", "dog"]}`

`group_by_length([])` → `{}`

## Tips
Use a dictionary with lengths as keys and lists as values.
