# Scale to Unit Range

## Description
Min-max normalization rescales numeric observations relative to their smallest and largest values, preserving their order.

## Requirements
- Implement `minmax_normalize(values)` in `starter/solution.py`.
- Return a new list with each value scaled into the inclusive range `[0, 1]`.
- Map the minimum to `0` and the maximum to `1` using the range between them.
- When every value is equal, return zeros for every position.
- Return `[]` for empty input without mutating it.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why does a constant dataset need a special case?
- What happens to values between the minimum and maximum?

## Example Behavior
`minmax_normalize([2, 4, 6])` → `[0, 0.5, 1]`

`minmax_normalize([3, 3])` → `[0, 0]`
