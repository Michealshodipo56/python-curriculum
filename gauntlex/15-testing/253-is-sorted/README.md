# Check the Order

## Description
Determine whether a sequence is already in nondecreasing order. Equal neighbors are permitted.

## Requirements
- Implement `is_sorted(values)` in `starter/solution.py`.
- Return `True` if each element is no smaller than the preceding one.
- Return `True` for empty and one-element sequences.
- Return `False` when any adjacent pair decreases.
- Do not sort or mutate the input.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips
- Why does an empty sequence count as sorted?

## Example Behavior
`is_sorted([1, 1, 3])` → `True`; `is_sorted([2, 1])` → `False`.
