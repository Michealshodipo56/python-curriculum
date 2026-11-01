# Numbers Hidden in Text

## Description
Find each uninterrupted run of ASCII digits inside a larger string and report the numeric values.

## Requirements
- Implement `extract_numbers(text)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`extract_numbers("a12 b003 c")` → `[12, 3]`

`extract_numbers("no digits")` → `[]`

## Tips
Think about what separates one number from the next and how leading zeros affect integer values.

Examples describe expected behavior without providing the implementation.
