# Text Segments

## Description
Divide a string into consecutive pieces of a maximum length without losing characters.

### Behavior contract
Split text into consecutive chunks of at most size characters. Raise ValueError if size is not positive.

## Requirements
- Implement `chunk_text(text, size)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`chunk_text("abcdef", 2)` → `["ab", "cd", "ef"]`

`chunk_text("abc", 5)` → `["abc"]`

## Tips
The last segment may be shorter. What should happen when the requested segment length is zero?

The examples show required behavior, not an implementation.
