# One Space Apart

## Description
Transform irregular whitespace into a consistent, readable separation between words.

## Requirements
- Implement `normalize_spaces(text)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`normalize_spaces("  hello   world \n")` → `"hello world"`

`normalize_spaces("\tA \t B\t")` → `"A B"`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
What counts as whitespace besides an ordinary space? Preserve the words while normalizing their boundaries.
