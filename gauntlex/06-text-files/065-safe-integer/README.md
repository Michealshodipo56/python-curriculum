# Parse With Care

## Description
Convert textual input into a base-ten integer when possible and provide a predictable result for invalid input.

## Requirements
- Implement `parse_integer(text)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`parse_integer("  -12 ")` → `-12`

`parse_integer("3.5")` → `None`

## Tips
Distinguish valid negative integers from decimal fractions and nonnumeric text.

Examples describe expected behavior without providing the implementation.
