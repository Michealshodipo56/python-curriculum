# Multiply and Accumulate

## Description
Combine two equal-length numeric vectors into a single scalar value.

### Behavior contract
Return the dot product of two equal-length numeric lists. Empty lists produce zero.

## Requirements
- Implement `dot_product(a, b)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`dot_product([1, 2, 3], [4, 5, 6])` → `32`

`dot_product([], [])` → `0`

## Tips
Pair elements by position rather than comparing every value with every other value.

Examples illustrate expected values, not a solution.
