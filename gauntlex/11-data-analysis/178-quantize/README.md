# quantize

## Challenge
Round each numeric value to the nearest multiple of positive step using Python's built-in round semantics.

## Requirements
- Implement `quantize(values, step)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`quantize([0.2, 0.7, 1.2], 0.5)` → `[0, 0.5, 1]`

`quantize([2, 4], 2)` → `[2, 4]`

## Hints
Scale by the step, round, then scale back.
