# lis_length

## Challenge
Return the length of the longest strictly increasing subsequence of integer values. Empty input returns zero. Target O(n log n) time.

## Requirements
- Implement `lis_length(values)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Hint
Maintain the smallest possible tail value for each subsequence length.

## Run tests
`python -m pytest tests -q`
