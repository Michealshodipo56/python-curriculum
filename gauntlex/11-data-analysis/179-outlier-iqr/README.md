# iqr_outliers

## Challenge
Return values strictly outside the fences Q1-1.5*IQR and Q3+1.5*IQR, preserving input order. Define Q1 and Q3 as medians of the lower and upper halves, excluding the overall median for odd N. Return [] when fewer than 4 values.

## Requirements
- Implement `iqr_outliers(values)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`iqr_outliers([1, 2, 2, 3, 100])` → `[100]`

`iqr_outliers([1, 2, 3])` → `[]`

## Hints
Sort a copy, split into halves, then compute the quartile medians.
