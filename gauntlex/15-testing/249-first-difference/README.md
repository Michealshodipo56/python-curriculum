# Find the Divergence

## Description

When comparing two sequences, identify the earliest point where their contents or lengths diverge.

## Requirements

- Implement `first_difference(a, b)` in `starter/solution.py`.
- Return the zero-based index of the first unequal pair.
- Return the shorter length if one sequence is a strict prefix of the other.
- Return `None` when the sequences are identical.
- Do not modify either sequence.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- What happens if every overlapping element matches but one sequence continues?

## Example Behavior

`first_difference([1, 2], [1, 3])` → `1`; `first_difference([1], [1, 2])` → `1`.
