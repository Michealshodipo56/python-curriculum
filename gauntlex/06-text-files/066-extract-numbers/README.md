# Numbers Hidden in Text

## Description
Find each uninterrupted run of ASCII digits inside a larger string and report the numeric values.

## Requirements
- Implement `extract_numbers(text)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`extract_numbers("a12 b003 c")` → `[12, 3]`

`extract_numbers("no digits")` → `[]`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
Think about what separates one number from the next and how leading zeros affect integer values.
