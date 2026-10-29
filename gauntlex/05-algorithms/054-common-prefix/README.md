# common_prefix

## Description
Return the longest prefix shared by every string in a list. Return empty string for an empty list.

## Requirements
- Implement `common_prefix(words)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`common_prefix(["flower", "flow", "flight"])` → `"fl"`

`common_prefix(["dog", "cat"])` → `""`

## Tips
Compare character positions while all words still agree.
