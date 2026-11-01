# Count Unique CSV Rows

## Description
Count distinct CSV data rows without treating the header as data.

### Behavior contract
Given a CSV file path with a header, return the number of unique data rows. Two rows are equal if every field matches, irrespective of record order. Assume valid CSV.

## Requirements
- Implement `csv_unique_rows(path)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Row equality depends on parsed field values, not the row's position.

The task defines behavior; design the implementation independently.
