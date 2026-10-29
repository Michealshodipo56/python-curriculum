# dense_ranks

## Challenge
Return dense ascending ranks for each input integer, with the smallest distinct value ranked 1. Equal values share a rank; there are no gaps.

## Requirements
- Implement `dense_ranks(values)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`dense_ranks([30, 10, 20, 10])` → `[3, 1, 2, 1]`

`dense_ranks([])` → `[]`

## Hints
Sort distinct values to build a rank lookup.
