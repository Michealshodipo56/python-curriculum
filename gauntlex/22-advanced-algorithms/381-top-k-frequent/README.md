# Frequency with Stable Ties

## Description
Rank distinct values by how often they occur, retaining first-seen order when frequencies match. This makes results reproducible without relying on sorting the values themselves.

## Requirements
- Implement `top_k_frequent(values, k)` in `starter/solution.py`.
- Input values are hashable; `k` is an integer.
- Return up to `k` distinct values ordered by descending occurrence count.
- For equal counts, rank the value first encountered in the input earlier.
- Raise `ValueError` for negative `k`; `k=0` returns an empty list.
- Do not mutate inputs or print.
- Use Python's standard library only.

## Design Considerations
Frequency ties require a deterministic ordering policy. Keep the count and tie-breaking rules distinct, and consider what should happen when k exceeds the number of distinct values.

## Tips
- What two pieces of information must be retained for each distinct value?
- What happens when `k` exceeds the number of distinct values?

## Example Behavior
`top_k_frequent(['b', 'a', 'b', 'a', 'c'], 2)` → `['b', 'a']`.
