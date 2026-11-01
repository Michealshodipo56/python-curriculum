# URL-Friendly Words

## Description
Convert a title into a lowercase, hyphen-separated identifier suitable for a simple URL path.

## Requirements
- Implement `slugify(text)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`slugify("Hello, Python World!")` → `"hello-python-world"`

`slugify("  A__B  ")` → `"a-b"`

## Tips
Several punctuation marks in a row should not create repeated separators.

Examples describe expected behavior without providing the implementation.
