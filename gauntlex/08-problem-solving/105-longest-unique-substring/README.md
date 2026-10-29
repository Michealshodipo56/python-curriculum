# longest_unique_substring

## Description
Return the length of the longest contiguous substring without repeated characters.

## Requirements
- Implement `longest_unique_substring(text)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`longest_unique_substring("abcabcbb")` → `3`

`longest_unique_substring("bbbbb")` → `1`

## Tips
Use a sliding window and remember the last index of each character.
