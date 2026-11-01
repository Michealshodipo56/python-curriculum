# Running Products

## Description
Produce the product of all values encountered up to each position.

### Behavior contract
Return running products of an integer list; empty input returns [].

## Requirements
- Implement `cumulative_product(values)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`cumulative_product([2, 3, 4])` → `[2, 6, 24]`

`cumulative_product([2, 0, 4])` → `[2, 0, 0]`

## Tips
Zero affects every later running product, even if subsequent values are nonzero.

Examples illustrate expected values, not a solution.
