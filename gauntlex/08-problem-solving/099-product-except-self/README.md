# Everyone Else's Product

## Description
Compute each position's product using all the other values, without division.

### Behavior contract
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
Zeros make shortcuts based on division unreliable. Consider contributions from both sides.

The examples define expected behavior; design your own implementation.
