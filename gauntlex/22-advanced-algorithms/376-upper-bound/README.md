# First Strictly Greater

## Description

Locate the insertion boundary immediately after all values equal to a target in an ascending sequence. Unlike a lower bound, equality must remain on the left of the answer.

## Requirements

- Implement `upper_bound(values, target)` in `starter/solution.py`.
- Assume ascending sorted values, including possible duplicates.
- Return the first index whose value is strictly greater than `target`; return `len(values)` when no such element exists.
- Use O(log n) comparisons; do not mutate inputs or print.
- Use Python's standard library only.

## Design Considerations

Locate the first element strictly greater than the target; equality belongs on the left side of the insertion boundary. Empty input and all-equal sequences are important boundary cases.

## Tips

- How should an equality comparison affect the search interval?
- What index should an empty sequence return?

## Example Behavior

`upper_bound([1, 2, 2, 5], 2)` → `3`; `upper_bound([], 2)` → `0`.
