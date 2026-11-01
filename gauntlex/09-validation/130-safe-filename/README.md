# Safe File Labels

## Description
Transform a human-readable label into a predictable ASCII filename stem.

### Behavior contract
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
What should remain when all characters are disallowed? The fallback name is part of the contract.

The examples specify results without giving an implementation.
