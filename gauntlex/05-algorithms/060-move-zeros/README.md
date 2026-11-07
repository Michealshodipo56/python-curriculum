# Zeros to the Back

## Description

Rearrange a sequence so that all numeric zeros appear after the nonzero values. Preserve the original order of nonzero elements.

## Requirements

- Implement `move_zeros(items)` in `starter/solution.py`.
- Accept a list of integers.
- Return a new list containing all nonzero elements in original order, followed by the same number of zeros.
- Preserve the input length and do not mutate `items`.
- Do not print or execute code on import.

## Tips

- What information must be preserved about the nonzero values?
- Consider all-zero, no-zero, and empty inputs.

## Example Behavior

`move_zeros([0, 1, 0, 3, 12])` → `[1, 3, 12, 0, 0]`; `move_zeros([0, 0])` → `[0, 0]`.
