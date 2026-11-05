# Dense Rankings

## Description
Assign ranks to integer observations by their numeric value. Equal values share a rank, and consecutive distinct values receive consecutive ranks without gaps.

## Requirements
- Implement `dense_ranks(values)` in `starter/solution.py`.
- Return a list of ranks in the original input order.
- Assign rank `1` to the smallest distinct value.
- Assign the same rank to equal values.
- Increase ranks by one for each next distinct value, without gaps.
- Return `[]` for empty input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why must ranking order differ from output order?
- What makes dense ranking different from ranking with skipped positions?

## Example Behavior
`dense_ranks([30, 10, 20, 10])` → `[3, 1, 2, 1]`

`dense_ranks([])` → `[]`
