# Longest Without Repeats

## Description
Find the length of the longest contiguous stretch of text containing no repeated characters.

### Behavior contract
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
A valid stretch can move forward without restarting from the beginning every time.

The examples define expected behavior; design your own implementation.
