# Count the Lines

## Description
Determine how many logical lines a string contains, including cases involving trailing line breaks.

## Requirements
- Implement `line_count(text)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`line_count("one\ntwo\n")` → `2`

`line_count("single")` → `1`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
Compare empty text, one line, and a line ending with a newline. Do they all count the same way?
