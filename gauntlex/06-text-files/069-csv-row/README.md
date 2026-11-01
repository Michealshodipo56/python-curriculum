# Fields and Quotes

## Description
Interpret one comma-separated record where quoted fields may contain commas or escaped quotation marks.

## Requirements
- Implement `parse_csv_row(line)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`parse_csv_row("a,b,c")` → `["a", "b", "c"]`

`parse_csv_row("\"a,b\",c")` → `["a,b", "c"]`

## Tips
A comma inside quotation marks is data, not a field boundary. Explore the CSV quoting rules.

Examples describe expected behavior without providing the implementation.
