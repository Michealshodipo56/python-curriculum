# Aggregate CSV Values

## Description
Tabular data often needs totals by category. Use CSV column names rather than fixed positions to group and sum numeric records.

## Requirements
- Implement `csv_group_sum(path, category_column, amount_column)` in `starter/solution.py`.
- Read the CSV file with its header row.
- Locate the category and amount columns by their supplied names.
- Treat amounts as valid integer strings and sum them by category.
- Return a category-to-integer-total dictionary; return `{}` when there are no data rows.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- What happens when the columns appear in a different order?

## Example Behavior
For rows `kind,amount` followed by `food,4` and `food,6`, the result is `{'food': 10}`.
