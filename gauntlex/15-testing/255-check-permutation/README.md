# Same Elements, New Order

## Description

Two sequences are permutations when they contain the same elements with identical occurrence counts, regardless of position.

## Requirements

- Implement `is_permutation(a, b)` in `starter/solution.py`.
- Accept lists of hashable elements.
- Return `True` only if both lists contain the same values with the same multiplicities.
- Treat ordering as irrelevant but duplicates as significant.
- Do not mutate either list.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips

- Why is comparing sets alone insufficient when values repeat?

## Example Behavior

`is_permutation([1, 2, 1], [1, 1, 2])` → `True`; `is_permutation([1, 1], [1, 2])` → `False`.
