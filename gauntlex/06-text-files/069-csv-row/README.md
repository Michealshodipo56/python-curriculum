# Fields and Quotes

## Description
Interpret one comma-separated record where quoted fields may contain commas or escaped quotation marks.

## Requirements
- Implement `parse_csv_row(line)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`parse_csv_row("a,b,c")` → `["a", "b", "c"]`

`parse_csv_row("\"a,b\",c")` → `["a,b", "c"]`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
A comma inside quotation marks is data, not a field boundary. Explore the CSV quoting rules.
