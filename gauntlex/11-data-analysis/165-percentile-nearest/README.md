# nearest_rank_percentile

## Challenge
Return the nearest-rank percentile for nonempty numeric values and integer p from 1 to 100 inclusive. Sort values; choose 1-based rank ceil(p*N/100).

## Requirements
- Implement `nearest_rank_percentile(values, p)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`nearest_rank_percentile([10, 20, 30, 40], 50)` → `20`

`nearest_rank_percentile([10, 20, 30, 40], 100)` → `40`

## Hints
Convert a 1-based rank to a zero-based index.
