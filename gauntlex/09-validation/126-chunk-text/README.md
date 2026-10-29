# chunk_text

## Description
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
Use string slices with a fixed step.
