# Count the Words

## Description

Words may be separated by spaces, tabs, or other whitespace. Determine how many words appear in a text without counting empty gaps.

## Requirements

- Implement `word_count(text)` in `starter/solution.py`.
- Count nonempty words separated by whitespace.
- Return `0` for empty or whitespace-only input.
- Return an integer; do not print or execute code on import.

## Tips

- How does repeated whitespace affect word boundaries?
- Check leading and trailing spaces, tabs, and empty text.

## Example Behavior

`word_count('one two three')` → `3`; `word_count('  a  b  ')` → `2`.
