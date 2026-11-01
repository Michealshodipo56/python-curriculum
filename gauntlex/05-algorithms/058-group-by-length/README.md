# Group by Size

## Description
Organize words into groups based on their character counts, preserving their encounter order within each group.

## Requirements
- Implement `group_by_length(words)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`group_by_length(["a", "cat", "be", "dog"])` → `{1: ["a"], 2: ["be"], 3: ["cat", "dog"]}`

`group_by_length([])` → `{}`

## Tips
What data structure lets you associate one length with several words?

The examples illustrate expected behavior, not an implementation.
