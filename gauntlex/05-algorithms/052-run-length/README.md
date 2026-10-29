# run_length

## Description
Encode a string as consecutive character/count pairs, represented as a list of two-element lists.

## Requirements
- Implement `run_length(text)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`run_length("aaabb")` → `[["a", 3], ["b", 2]]`

`run_length("abc")` → `[["a", 1], ["b", 1], ["c", 1]]`

## Tips
Count repeated adjacent characters, then start a new run when the character changes.
