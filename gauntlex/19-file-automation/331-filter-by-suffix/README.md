# Select File Types

## Description
Filter a sequence of filenames by final extension without changing the filenames or their order.

## Requirements
- Implement `filter_suffix(names, suffix)` in `starter/solution.py`.
- Accept filenames and a suffix that includes its leading dot.
- Match the final suffix case-insensitively.
- Return the original matching filenames in input order.
- Do not match a similar substring that is not the final suffix.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Match the complete final suffix without treating a similar substring in the middle of a filename as a match. Keep original filenames and input ordering while comparing without case sensitivity.

## Tips
- Why should `report.csv.bak` not match a `.csv` filter?

## Example Behavior
`filter_suffix(['A.CSV', 'b.txt', 'c.csv'], '.csv')` → `['A.CSV', 'c.csv']`.
