# Fit a Straight Line

## Description

Find the least-squares straight line that best describes paired numeric observations, expressed as a slope and intercept.

## Requirements

- Implement `linear_regression(xs, ys)` in `starter/solution.py`.
- Assume equal-length numeric `xs` and `ys` containing at least two points.
- Return `[slope, intercept]` for the ordinary least-squares line `y = slope * x + intercept`.
- Return `None` when all `x` values are equal.
- Do not mutate the input lists.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips

- What does the slope describe about changes in `x` and `y`?
- Why can a vertical set of observations not be represented by this form?

## Example Behavior

`linear_regression([1, 2, 3], [2, 4, 6])` → `[2, 0]`

`linear_regression([1, 1], [2, 3])` → `None`
