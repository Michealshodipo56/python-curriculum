# top_words

## Description
Return the n most frequent lowercase ASCII words in text, ordered by descending count and then alphabetically. Words are maximal runs of letters a-z; ignore punctuation. Assume n>=0.

## Requirements
- Implement `top_words(text, n)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`top_words("Red red blue!", 2)` → `["red", "blue"]`

`top_words("b a b a", 1)` → `["a"]`

## Tips
Normalize and tokenize before counting; a secondary alphabetical key resolves ties.
