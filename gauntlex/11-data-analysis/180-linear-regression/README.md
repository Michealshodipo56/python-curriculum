# Fit a Straight Line

## Description
Estimate a slope and intercept for a least-squares line through numeric observations.

### Behavior contract
Return [slope,intercept] for ordinary least-squares fit y=slope*x+intercept on equal-length numeric lists with at least two points. Return None if all x values are equal.

## Requirements
- Implement `linear_regression(xs, ys)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`linear_regression([1, 2, 3], [2, 4, 6])` → `[2, 0]`

`linear_regression([1, 1], [2, 3])` → `None`

## Tips
A vertical collection of points has no unique slope in this representation.

Examples illustrate expected values, not a solution.
