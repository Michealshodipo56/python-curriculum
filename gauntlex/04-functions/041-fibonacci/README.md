# Sequence Memory

## Description
In the Fibonacci sequence, each term after the first two is the sum of the two preceding terms. Write a function that finds a requested term without displaying intermediate values.

## Requirements
- Implement `fibonacci(n)` in `solution.py`.
- Assume `n` is a nonnegative integer.
- Use the definition F(0) = 0, F(1) = 1, and F(n) = F(n−1) + F(n−2).
- Return the nth term as an integer.
- Do not print or execute input-handling code on import.

## Tips
- Which previous terms are needed to determine the next one?
- Why are the first two terms special?
- Trace a short sequence before generalizing.

## Example Behavior
`fibonacci(0)` → `0`; `fibonacci(1)` → `1`; `fibonacci(6)` → `8`.
