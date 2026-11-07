# Running Products

## Description

Track how the product of a sequence changes as each additional integer is included. Return one product for every prefix.

## Requirements

- Implement `cumulative_product(values)` in `starter/solution.py`.
- Return a new list of running products in input order.
- At each position, include every integer from the beginning through that position.
- Return `[]` for empty input.
- Do not mutate the original list.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips

- What effect does a zero have on all later running products?
- How is this different from multiplying every value only once for a single result?

## Example Behavior

`cumulative_product([2, 3, 4])` → `[2, 6, 24]`

`cumulative_product([2, 0, 4])` → `[2, 0, 0]`
