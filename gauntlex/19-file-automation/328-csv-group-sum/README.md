# csv_group_sum

## Challenge
Given a CSV file path with a header, category column name, and integer amount column name, return a dictionary mapping categories to summed amounts. Empty data produces {}. Assume valid CSV and integers.

## Requirements
- Implement `csv_group_sum(path, category_column, amount_column)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
DictReader handles header-based column lookup.

## Run tests
`python -m pytest tests -q`
