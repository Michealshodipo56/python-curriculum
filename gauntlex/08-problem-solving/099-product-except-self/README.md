# product_except_self

## Description
Return a list where each position contains the product of all other integers. Do not use division.

## Requirements
- Implement `product_except_self(nums)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`product_except_self([1, 2, 3, 4])` → `[24, 12, 8, 6]`

`product_except_self([0, 1, 2])` → `[2, 0, 0]`

## Tips
Prefix and suffix products avoid division and handle zeros.
