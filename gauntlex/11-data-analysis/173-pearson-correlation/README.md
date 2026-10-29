# pearson_correlation

## Challenge
Return Pearson correlation of two equal-length numeric lists of length >=2. Return None if either list has zero variance.

## Requirements
- Implement `pearson_correlation(a, b)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`pearson_correlation([1, 2, 3], [2, 4, 6])` → `1`

`pearson_correlation([1, 1, 1], [2, 3, 4])` → `None`

## Hints
Center each vector and normalize the sum of cross-products.
