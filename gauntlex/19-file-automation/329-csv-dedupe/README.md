# Count Unique CSV Rows

## Description
A CSV file may repeat complete data rows. Count distinct parsed records while excluding the header from the data.

## Requirements
- Implement `csv_unique_rows(path)` in `starter/solution.py`.
- Read a valid CSV file with a header.
- Compare data rows by all parsed field values, regardless of row order.
- Return the number of distinct data rows as an integer.
- Do not count the header as a data row.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Compare the entire parsed row, not the original CSV text or one selected field. Identical rows count once regardless of where they occur, while the header is never a data record.

## Tips
- Why is comparing only one field insufficient for full-row deduplication?

## Example Behavior
For data rows `a,1`, `a,1`, and `a,2`, the unique row count is `2`.
