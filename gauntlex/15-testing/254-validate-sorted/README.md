# Reject Disorder

## Description

Validation checks a property of existing data; it must not silently repair the data by sorting it.

## Requirements

- Implement `validate_sorted(values)` in `starter/solution.py`.
- Return the original list unchanged when values are nondecreasing.
- Raise `ValueError` if any later value is smaller than the previous one.
- Do not mutate the list or return a sorted copy.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips

- Why should validation reject rather than repair unordered data?

## Example Behavior

`validate_sorted([1, 2, 2])` returns the original list; `validate_sorted([2, 1])` raises `ValueError`.
