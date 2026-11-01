# Aggregate CSV Values

## Description
Summarize numeric CSV records by a named category column.

### Behavior contract
Given a CSV file path with a header, category column name, and integer amount column name, return a dictionary mapping categories to summed amounts. Empty data produces {}. Assume valid CSV and integers.

## Requirements
- Implement `csv_group_sum(path, category_column, amount_column)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Use header names to locate fields rather than fixed column positions.

The task defines behavior; design the implementation independently.
