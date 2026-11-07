# First Not Smaller

## Description
Search a sorted collection for the first position at which a target could be inserted without placing it after an equal value. The result is an insertion boundary, even when the target is absent.

## Requirements
- Implement `lower_bound(values, target)` in `starter/solution.py`.
- Assume `values` is sorted in ascending order and may contain duplicates.
- Return the index of the first element greater than or equal to `target`; return `len(values)` if there is none.
- Use O(log n) comparisons; do not mutate the input or print output.
- Use Python's standard library only.

## Design Considerations
Maintain a half-open search interval whose left boundary is the earliest possible valid insertion point. Equal elements must push the search toward earlier positions, not terminate it.

## Tips
- What does the boundary mean when all elements are smaller than the target?
- Which half can be discarded when a middle value equals the target?

## Example Behavior
`lower_bound([1, 2, 2, 5], 2)` → `1`; `lower_bound([1, 2], 3)` → `2`.
