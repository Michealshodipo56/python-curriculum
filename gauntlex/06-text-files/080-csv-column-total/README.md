# Sum a CSV Column

## Description

CSV reports often reorder columns and contain cells that cannot be used as numbers. Locate the requested column by its header and accumulate valid integer values.

## Requirements

- Implement `csv_column_total(path, column)` in `starter/solution.py`.
- Accept the CSV file path and the name of the column to total.
- Read the CSV with UTF-8 encoding and identify the target column by its header, not a fixed index.
- Add valid integer values from that column and return the numeric total.
- Do not hardcode paths, print results, or alter the input file.
- Use Python's standard library only. Do not mutate caller-owned inputs.
- Assume the named column exists in a well-formed CSV header. Ignore empty, missing, or noninteger data cells in that column; negative integers contribute to the total. Return `0` when no valid values occur.

## Tips

- What happens when the requested column moves to another position?
- How should empty or noninteger cells affect the running total?

## Example Behavior

For a CSV file containing a header `name,amount` and rows `Ada,4` and `Lin,-2`, `csv_column_total(path, 'amount')` returns `2`.

Rows with `amount` values `4`, empty, `unknown`, and `-2` also total `2`: the empty and noninteger cells are skipped. A header with no data rows totals `0`.
