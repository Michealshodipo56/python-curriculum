# Division Without Failure

## Description
Provide a division operation that handles a zero divisor without terminating unexpectedly.

## Requirements
- Implement `safe_divide(a, b)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`safe_divide(8, 2)` → `4`

`safe_divide(3, 0)` → `None`

## Tips
- Identify the expected input, output, and failure or empty-data behavior before implementing the function.
- Check the exact behavior at boundaries, not only typical inputs.
The zero-divisor case is expected. How should it differ from ordinary division?
