# Linear Relationship

## Description

Pearson correlation measures the direction and strength of a linear relationship between two paired numeric datasets.

## Requirements

- Implement `pearson_correlation(a, b)` in `starter/solution.py`.
- Assume two equal-length numeric lists containing at least two observations.
- Return the Pearson correlation coefficient of the paired observations.
- Return `None` if either dataset has zero variance.
- Do not mutate either input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips

- Why does a constant dataset prevent correlation from being calculated?
- What do positive and negative correlation indicate?

## Example Behavior

`pearson_correlation([1, 2, 3], [2, 4, 6])` → `1`

`pearson_correlation([1, 1, 1], [2, 3, 4])` → `None`
