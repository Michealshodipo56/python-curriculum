# top_k_frequent

## Description
Return the k most frequent integers, ordered by decreasing frequency and then increasing numeric value. Assume 0<=k<=number of distinct values.

## Requirements
- Implement `top_k_frequent(nums, k)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`top_k_frequent([1, 1, 1, 2, 2, 3], 2)` → `[1, 2]`

`top_k_frequent([4, 4, 5, 5, 3], 2)` → `[4, 5]`

## Tips
Count values, then sort by a compound frequency/value key.
