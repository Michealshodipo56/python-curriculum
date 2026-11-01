# Linear Relationship

## Description
Measure the direction and strength of the linear relationship between two numeric datasets.

### Behavior contract
Return Pearson correlation of two equal-length numeric lists of length >=2. Return None if either list has zero variance.

## Requirements
- Implement `pearson_correlation(a, b)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`pearson_correlation([1, 2, 3], [2, 4, 6])` → `1`

`pearson_correlation([1, 1, 1], [2, 3, 4])` → `None`

## Tips
A dataset with no variation cannot support this correlation calculation.

Examples illustrate expected values, not a solution.
