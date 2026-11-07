# Greatest Shared Divisor

## Description
Find the greatest nonnegative integer that divides two integers without a remainder. The function must handle negative inputs and zero correctly.

## Requirements
- Implement `gcd(a, b)` in `solution.py`.
- Accept any two integers, including negative values and zero.
- Return a nonnegative greatest common divisor.
- Return `0` for two zero arguments.
- Return the result without printing or running input-handling code on import.

## Tips
- How does the remainder of two numbers relate to their common divisors?
- Why does changing a number's sign not change the answer?
- Consider when one argument is zero.

## Example Behavior
`gcd(12, 18)` → `6`; `gcd(-8, 12)` → `4`; `gcd(0, 0)` → `0`.
