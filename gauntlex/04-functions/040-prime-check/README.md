# Prime or Composite

## Description
Prime numbers have exactly two positive divisors: one and themselves. Build a function that identifies primes while correctly rejecting zero, one, and negative integers.

## Requirements
- Implement `is_prime(n)` in `solution.py`.
- Return `True` exactly when integer `n` is prime.
- Return `False` for every integer below 2.
- Return a boolean without printing or executing input-handling code on import.

## Tips
- What does finding one divisor other than one and the number prove?
- Can you avoid checking every smaller integer?
- Consider 2, 4, 9, and 17.

## Example Behavior
`is_prime(2)` → `True`; `is_prime(17)` → `True`; `is_prime(1)` → `False`.
