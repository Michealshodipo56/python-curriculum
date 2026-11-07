# Guard the Nonnegative Invariant

## Description

An invariant is a condition that must remain true for a collection of values. Detect the earliest violation and report its location.

## Requirements

- Implement `check_nonnegative(values)` in `starter/solution.py`.
- Accept a sequence of numeric values.
- Return `True` if every value is nonnegative.
- Otherwise raise `AssertionError` with exact message `negative at INDEX` for the first negative value's zero-based index.
- Do not mutate the sequence.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why should the first violation be reported instead of every violation?

## Example Behavior

`check_nonnegative([0, 3])` → `True`; `check_nonnegative([1, -2, -3])` raises `AssertionError('negative at 1')`.
