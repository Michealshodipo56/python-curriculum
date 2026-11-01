# Scale to Unit Range

## Description
Rescale observations so the smallest maps to zero and the largest to one.

### Behavior contract
Return values normalized into [0,1] by (x-min)/(max-min). If all values are equal, return a list of zeros. Empty input returns [].

## Requirements
- Implement `minmax_normalize(values)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`minmax_normalize([2, 4, 6])` → `[0, 0.5, 1]`

`minmax_normalize([3, 3])` → `[0, 0]`

## Tips
When all values are equal, the range is zero and needs a defined result.

Examples illustrate expected values, not a solution.
