# Find the Divergence

## Description
Locate the first position where two sequences disagree.

### Behavior contract
Return the zero-based index of the first differing element in two sequences. Return None if equal. If one is a strict prefix of the other, return the shorter length.

## Requirements
- Implement `first_difference(a, b)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
One sequence can end while the other still has elements.

Work from the contract and edge cases; do not include a finished implementation.
