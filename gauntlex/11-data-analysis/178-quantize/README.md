# Round to Steps

## Description
Quantization maps numeric observations to the nearest multiple of a positive step. The rounding rule must follow Python's built-in semantics.

## Requirements
- Implement `quantize(values, step)` in `starter/solution.py`.
- Assume `step` is positive.
- Return a new list with every value rounded to the nearest multiple of `step`.
- Use Python's built-in `round` semantics, including midpoint behavior.
- Preserve input order and do not mutate it.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why can midpoint values behave differently from always rounding upward?
- How does changing the step alter the available results?

## Example Behavior
`quantize([0.2, 0.7, 1.2], 0.5)` → `[0, 0.5, 1]`

`quantize([2, 4], 2)` → `[2, 4]`
