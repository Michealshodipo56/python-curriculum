# Text Segments

## Description
Divide a string into consecutive pieces of a requested maximum length. Preserve every character and the original order.

## Requirements
- Implement `chunk_text(text, size)` in `starter/solution.py`.
- Return a list of consecutive substrings of length at most `size`.
- Require `size` to be a positive integer; raise `ValueError` otherwise.
- Allow the final piece to be shorter than the others.
- Return `[]` for empty text.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- What happens when the text length is not a multiple of the chunk size?
- Why must zero or negative chunk lengths be rejected?

## Example Behavior
`chunk_text('abcdef', 2)` → `['ab', 'cd', 'ef']`; `chunk_text('abc', 5)` → `['abc']`.
