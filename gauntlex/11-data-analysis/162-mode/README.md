# mode

## Challenge
Return the most frequent integer; break ties by choosing the smallest integer. Assume nonempty input.

## Requirements
- Implement `mode(values)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`mode([2, 3, 2, 3])` → `2`

`mode([5, 5, 1])` → `5`

## Hints
A frequency table and deterministic tie-break avoid order dependence.
