# Sliding Average

## Description
Compute the average of every consecutive fixed-length window.

### Behavior contract
Return a list of averages of each consecutive window of size k. Assume k is positive; return [] if k exceeds input length.

## Requirements
- Implement `moving_average(values, k)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`moving_average([1, 2, 3, 4], 2)` → `[1.5, 2.5, 3.5]`

`moving_average([1, 2], 3)` → `[]`

## Tips
Adjacent windows share most of their elements; consider what information can be reused.

Examples illustrate expected values, not a solution.
