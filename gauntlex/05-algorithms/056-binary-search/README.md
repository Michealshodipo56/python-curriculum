# Halve the Search

## Description

A sorted collection can be searched efficiently by repeatedly ruling out half of the remaining candidates. Find the index of a target value using this approach.

## Requirements

- Implement `binary_search(items, target)` in `starter/solution.py`.
- Assume `items` is sorted in ascending order and contains distinct integers.
- Return the zero-based index of `target`, or `-1` when absent.
- Use a search that narrows the candidate interval rather than checking every item in order.
- Do not modify input, print, or execute code on import.

## Tips

- How does a comparison with the middle value eliminate part of the search space?
- What does it mean when no candidate positions remain?

## Example Behavior

`binary_search([1, 3, 5, 7], 5)` → `2`; `binary_search([1, 3, 5], 2)` → `-1`.
