# Increasing Subsequence

## Description
Find the maximum length of a strictly increasing subsequence while preserving the original relative order. Elements in a subsequence need not be adjacent.

## Requirements
- Implement `lis_length(values)` in `starter/solution.py`.
- Return the length of the longest strictly increasing subsequence of integer values.
- Equal consecutive chosen values do not count as increasing.
- Return `0` for empty input.
- Target O(n log n) time; do not mutate inputs or print.
- Use Python's standard library only.

## Design Considerations
Increasing means strictly greater, so equal values cannot extend a subsequence. Preserve the original order of selected elements even though they need not be adjacent.

## Tips
- How is a subsequence different from a contiguous substring?
- What compact information could represent promising subsequences without storing them all?

## Example Behavior
`lis_length([10, 9, 2, 5, 3, 7, 101, 18])` → `4`; `lis_length([])` → `0`.
