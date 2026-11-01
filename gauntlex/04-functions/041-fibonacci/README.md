# Sequence Memory

## Description
Compute one term of a sequence where every term after the first two depends on the two preceding terms.

## Requirements
- Implement ``fibonacci(n)`` in `solution.py`.
- For nonnegative `n`, return the nth term with F(0)=0, F(1)=1, and F(n)=F(n−1)+F(n−2).
- Return the result instead of printing it.
- Do not run input-handling code when the module is imported.

## Example
`fibonacci(0)` → `0`; `fibonacci(1)` → `1`; `fibonacci(6)` → `8`.

## Tips
Track how much previous information is necessary to produce the next term.

The examples specify behavior without supplying the implementation.
