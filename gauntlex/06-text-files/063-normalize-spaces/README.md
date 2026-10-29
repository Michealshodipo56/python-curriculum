# normalize_spaces

## Description
Replace each run of whitespace with one ASCII space and trim the ends.

## Requirements
- Implement `normalize_spaces(text)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`normalize_spaces("  hello   world \n")` → `"hello world"`

`normalize_spaces("\tA \t B\t")` → `"A B"`

## Tips
Split text on whitespace and join with one space.
