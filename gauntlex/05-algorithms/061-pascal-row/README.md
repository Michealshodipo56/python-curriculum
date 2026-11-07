# Build Pascal's Row

## Description
Pascal's triangle grows one row at a time. Every row begins and ends with one, while interior entries are formed from neighboring values in the preceding row.

## Requirements
- Implement `pascal_row(n)` in `solution.py`.
- Assume `n` is a nonnegative integer and row numbering begins at zero.
- Return the full nth row as a list of integers.
- Row zero is `[1]`; each later row contains `n + 1` entries.
- Do not print or execute code on import.

## Tips
- How do the first and last values differ from the interior values?
- Trace the first few rows and identify how their lengths change.

## Example Behavior
`pascal_row(0)` → `[1]`; `pascal_row(1)` → `[1, 1]`; `pascal_row(4)` → `[1, 4, 6, 4, 1]`.
