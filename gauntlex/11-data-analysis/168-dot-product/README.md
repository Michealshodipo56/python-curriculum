# Multiply and Accumulate

## Description
The dot product combines two numeric vectors by pairing corresponding positions and adding their products.

## Requirements
- Implement `dot_product(a, b)` in `starter/solution.py`.
- Assume `a` and `b` are equal-length numeric lists.
- Multiply the elements at matching indices and sum those products.
- Return a single numeric result.
- Return `0` for two empty vectors; do not mutate either list.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why must vector elements be paired by position?
- How does the empty case affect the total?

## Example Behavior
`dot_product([1, 2, 3], [4, 5, 6])` → `32`

`dot_product([], [])` → `0`
