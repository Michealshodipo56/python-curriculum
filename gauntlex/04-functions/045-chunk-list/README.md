# Divide Into Chunks

## Description

In `starter/solution.py`, write `chunks(items, size)` to split a list into consecutive smaller lists containing at most `size` elements. For example, splitting `[1, 2, 3, 4, 5]` with size `2` produces `[[1, 2], [3, 4], [5]]`.

## Requirements

- Implement `chunks(items, size)` in `starter/solution.py`.
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
