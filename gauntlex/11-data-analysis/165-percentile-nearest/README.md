# Nearest-Rank Percentile

## Description

A percentile selects an observation at a specified position in sorted data. Use the nearest-rank definition rather than interpolation.

## Requirements

- Implement `nearest_rank_percentile(values, p)` in `starter/solution.py`.
- Assume `values` is nonempty and `p` is an integer from `1` through `100`.
- Sort the values conceptually in ascending order without mutating the input.
- Choose the one-based rank `ceil(p * N / 100)` for `N` observations.
- Return the value at that rank.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips

- Why does the percentile rank start at one rather than zero?
- What does the 100th percentile select?

## Example Behavior

`nearest_rank_percentile([10, 20, 30, 40], 50)` → `20`

`nearest_rank_percentile([10, 20, 30, 40], 100)` → `40`
