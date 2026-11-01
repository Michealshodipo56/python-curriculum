# Frequency with Stable Ties

## Description
Rank the most frequent values while resolving ties by first appearance.

### Behavior contract
Given hashable values and nonnegative integer k, return up to k distinct values ordered by descending frequency, breaking ties by the index of their first appearance. Raise ValueError for negative k.

## Requirements
- Implement `top_k_frequent(values, k)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Tips
Frequency and encounter order both influence the final ranking.

The task is to design an implementation that meets both behavior and efficiency requirements.
