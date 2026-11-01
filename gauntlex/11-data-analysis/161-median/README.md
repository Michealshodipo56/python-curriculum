# The Middle Value

## Description
Find the center of a dataset, averaging two central values when its size is even.

### Behavior contract
Return the median of a nonempty list of numbers. For even length, average the two middle values. Do not mutate the input.

## Requirements
- Implement `median(values)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`median([3, 1, 2])` → `2`

`median([4, 1, 3, 2])` → `2.5`

## Tips
The middle depends on numeric order, not original position.

Examples illustrate expected values, not a solution.
