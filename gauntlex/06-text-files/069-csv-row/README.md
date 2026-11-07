# Fields and Quotes

## Description

A comma-separated row may contain quoted fields whose commas are data rather than separators. Interpret one complete record using CSV quoting conventions.

## Requirements

- Implement `parse_csv_row(line)` in `starter/solution.py`.
- Return the parsed fields of the supplied CSV record as a list of strings.
- Respect quoted commas and doubled quotation marks inside quoted fields.
- Preserve empty fields and their positions; use Python's standard library.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.
- Assume one well-formed CSV record. Keep field whitespace as data; do not perform extra trimming.

## Tips

- Why does splitting on every comma fail for a quoted field?
- How are quotation marks represented inside a quoted CSV value?

## Example Behavior

`parse_csv_row("a,b,c")` → `["a", "b", "c"]`

`parse_csv_row("a,,c")` → `["a", "", "c"]`

`parse_csv_row("\"a,b\",c")` → `["a,b", "c"]`
