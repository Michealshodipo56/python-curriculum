# Circular Shift

## Description
A rotation moves items from the end of a list to the beginning while preserving their relative order. Build a function that handles shifts longer than the list itself.

## Requirements
- Implement `rotate_right(items, k)` in `solution.py`.
- Assume `k` is a nonnegative integer.
- Return a new list rotated right by `k` positions.
- Return an empty list for empty input and do not modify `items`.
- Do not print or execute code on import.

## Tips
- What happens after a full rotation?
- How can a large shift be related to the list length?
- Consider zero shifts.

## Example Behavior
`rotate_right([1, 2, 3, 4], 1)` → `[4, 1, 2, 3]`; `rotate_right([1, 2], 5)` → `[2, 1]`.
