# Parse With Care

## Description

User-entered numbers are not always valid integers. Convert valid base-ten integer text while giving callers a predictable nonexceptional result for invalid input.

## Requirements

- Implement `parse_integer(text)` in `starter/solution.py`.
- Accept surrounding whitespace and an optional leading sign on a valid integer.
- Return the parsed integer for valid decimal integer text.
- Return `None` for text that cannot be interpreted as a base-ten integer, including fractional notation.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips

- How should `-12` differ from `3.5`?
- What should happen with empty or whitespace-only input?

## Example Behavior

`parse_integer("  -12 ")` → `-12`

`parse_integer("3.5")` → `None`
