# Longest in the Line

## Description
Find the longest word in a text. If several words have the same maximum length, keep the first one encountered.

## Requirements
- Implement `longest_word(text)` in `solution.py`.
- Treat words as nonempty whitespace-separated tokens.
- Return the longest word; for ties return the earliest.
- Return an empty string if there are no words.
- Do not print or execute code on import.

## Tips
- How should the current winner change when a longer word appears?
- Why should a tie not replace the earlier winner?

## Example Behavior
`longest_word('cat elephant dog')` → `'elephant'`; `longest_word('aa bb')` → `'aa'`.
