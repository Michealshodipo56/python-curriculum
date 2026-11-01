# Reject Disorder

## Description
Accept an already sorted list unchanged and reject an unsorted one.

### Behavior contract
Return the original list unchanged when it is nondecreasing; otherwise raise ValueError. Do not mutate input.

## Requirements
- Implement `validate_sorted(values)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Validation should not quietly repair the caller's data.

Work from the contract and edge cases; do not include a finished implementation.
