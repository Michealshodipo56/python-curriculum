# longest_word

## Description
Return the longest whitespace-separated word in a string. On ties, return the first. Return an empty string when no words exist.

## Requirements
- Implement `longest_word(text)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`longest_word("cat elephant dog")` → `"elephant"`

`longest_word("aa bb")` → `"aa"`

## Tips
Keep a current best word and update only for strictly greater length.
