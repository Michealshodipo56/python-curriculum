# top_k_frequent

## Challenge
Given hashable values and nonnegative integer k, return up to k distinct values ordered by descending frequency, breaking ties by the index of their first appearance. Raise ValueError for negative k.

## Requirements
- Implement `top_k_frequent(values, k)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Hint
Keep frequency counts and first occurrence indices.

## Run tests
`python -m pytest tests -q`
