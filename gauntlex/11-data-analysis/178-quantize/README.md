# Round to Steps

## Description
Snap numeric observations to the nearest multiple of a positive step.

### Behavior contract
Round each numeric value to the nearest multiple of positive step using Python's built-in round semantics.

## Requirements
- Implement `quantize(values, step)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`quantize([0.2, 0.7, 1.2], 0.5)` → `[0, 0.5, 1]`

`quantize([2, 4], 2)` → `[2, 4]`

## Tips
Rounding at a midpoint follows Python's built-in behavior; do not invent a different tie rule.

Examples illustrate expected values, not a solution.
