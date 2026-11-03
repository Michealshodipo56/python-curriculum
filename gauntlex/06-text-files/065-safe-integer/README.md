# Parse With Care

## Description
Convert textual input into a base-ten integer when possible and provide a predictable result for invalid input.

## Requirements
- Implement `parse_integer(text)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`parse_integer("  -12 ")` → `-12`

`parse_integer("3.5")` → `None`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
Distinguish valid negative integers from decimal fractions and nonnumeric text.
