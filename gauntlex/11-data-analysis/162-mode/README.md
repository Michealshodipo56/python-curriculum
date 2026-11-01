# Most Frequent Observation

## Description
Identify the most common integer and apply a deterministic rule when several values tie.

### Behavior contract
Return the most frequent integer; break ties by choosing the smallest integer. Assume nonempty input.

## Requirements
- Implement `mode(values)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`mode([2, 3, 2, 3])` → `2`

`mode([5, 5, 1])` → `5`

## Tips
Count occurrences first, then decide how ties should be resolved.

Examples illustrate expected values, not a solution.
