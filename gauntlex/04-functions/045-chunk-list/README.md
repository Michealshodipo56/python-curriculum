# Divide Into Chunks

## Description
Partition a sequence into consecutive groups of a requested maximum size. Preserve the order of elements, and allow the final group to be shorter.

## Requirements
- Implement `chunks(items, size)` in `solution.py`.
- Assume `size` is a positive integer.
- Return a new list of consecutive sublists, each containing at most `size` elements.
- Preserve input order, return an empty list for empty input, and do not modify `items`.
- Return the result without printing or running input-handling code on import.

## Tips
- What happens when the input length is not divisible by the chunk size?
- How do you identify consecutive group boundaries?
- Consider when the group size is larger than the entire collection.

## Example Behavior
`chunks([1, 2, 3, 4, 5], 2)` → `[[1, 2], [3, 4], [5]]`.
