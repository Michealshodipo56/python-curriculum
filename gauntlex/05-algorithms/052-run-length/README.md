# Compress Repeated Runs

## Description
Describe a string as a sequence of adjacent character runs. Each run records its character and how many times it appears consecutively.

## Requirements
- Implement `run_length(text)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`run_length("aaabb")` → `[["a", 3], ["b", 2]]`

`run_length("abc")` → `[["a", 1], ["b", 1], ["c", 1]]`

## Tips
Two runs of the same character may be separated by another character; they should not be combined.

The examples illustrate the contract without providing an implementation.
