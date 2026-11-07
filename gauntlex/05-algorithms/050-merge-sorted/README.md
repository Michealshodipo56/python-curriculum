# Two Ordered Streams

## Description

Combine two already sorted lists into one sorted list. Preserve every value, including duplicates, without changing the original inputs.

## Requirements

- Implement `merge_sorted(left, right)` in `starter/solution.py`.
- Assume both input lists are sorted in ascending numeric order.
- Return a new ascending list containing every element of both inputs.
- Preserve duplicates and handle empty lists.
- Do not modify inputs, print, or execute code on import.

## Tips

- Compare the next unconsumed values from each list.
- What happens when one list has no elements left?
- How should equal values be handled?

## Example Behavior

`merge_sorted([1, 3, 5], [2, 4])` → `[1, 2, 3, 4, 5]`; `merge_sorted([], [-1, 2])` → `[-1, 2]`.
