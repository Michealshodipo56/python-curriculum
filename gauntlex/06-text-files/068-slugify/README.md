# URL-Friendly Words

## Description
Convert a title into a lowercase, hyphen-separated identifier suitable for a simple URL path.

## Requirements
- Implement `slugify(text)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`slugify("Hello, Python World!")` → `"hello-python-world"`

`slugify("  A__B  ")` → `"a-b"`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
Several punctuation marks in a row should not create repeated separators.
