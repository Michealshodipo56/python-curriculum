# Division Without Failure

## Description

A reusable numeric operation should handle an expected zero divisor without crashing the caller. Preserve ordinary division behavior for valid divisors.

## Requirements

- Implement `safe_divide(a, b)` in `starter/solution.py`.
- Return the result of dividing `a` by `b` when the divisor is nonzero.
- Return `None` when `b` is zero rather than raising a division-by-zero exception.
- Do not change the operands or print a result.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips

- What is the difference between a valid zero quotient and an invalid zero divisor?
- Which failure condition does this function explicitly handle?

## Example Behavior

`safe_divide(8, 2)` → `4`

`safe_divide(3, 0)` → `None`
