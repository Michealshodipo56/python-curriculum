# Sequence Memory

## Description

In `starter/solution.py`, write `fibonacci(n)` to return the number at position `n` in the Fibonacci sequence, which starts `0, 1, 1, 2, 3, 5, 8, ...`. Position `0` returns `0`, and position `1` returns `1`.

## Requirements

- Implement `fibonacci(n)` in `starter/solution.py`.
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
