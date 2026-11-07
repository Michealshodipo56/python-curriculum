# Longest Without Repeats

## Description

A substring is a contiguous stretch of text. Determine the maximum length of a substring in which no character appears more than once.

## Requirements

- Implement `longest_unique_substring(text)` in `starter/solution.py`.
- Return the length of the longest contiguous substring without repeated characters.
- Treat character comparisons as case-sensitive.
- Return `0` for empty text.
- Do not alter the original string.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- Why is a substring different from a subsequence?
- What happens to a candidate stretch when a character repeats?

## Example Behavior

`longest_unique_substring('abcabcbb')` → `3`; `longest_unique_substring('bbbbb')` → `1`.
