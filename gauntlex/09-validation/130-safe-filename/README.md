# safe_filename

## Description
Convert an ASCII label into a lowercase filename stem by replacing each run of characters other than a-z, 0-9, underscore, or hyphen with one underscore. Trim leading/trailing underscores. Return 'untitled' if empty.

## Requirements
- Implement `safe_filename(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`safe_filename("My Report (2024)")` → `"my_report_2024"`

`safe_filename("!!!")` → `"untitled"`

## Tips
Decide which characters to preserve before applying a replacement pattern.
