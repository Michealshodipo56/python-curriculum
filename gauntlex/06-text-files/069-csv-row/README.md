# parse_csv_row

## Description
Parse a single CSV record into fields, supporting quoted commas and doubled quotes.

## Requirements
- Implement `parse_csv_row(line)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`parse_csv_row("a,b,c")` → `["a", "b", "c"]`

`parse_csv_row("\"a,b\",c")` → `["a,b", "c"]`

## Tips
The standard library csv reader supports quoting.
