# slugify

## Description
Convert ASCII text to lowercase; replace each run of non-alphanumeric characters with a hyphen and trim outer hyphens.

## Requirements
- Implement `slugify(text)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`slugify("Hello, Python World!")` → `"hello-python-world"`

`slugify("  A__B  ")` → `"a-b"`

## Tips
Normalize case and use a replacement pattern.
