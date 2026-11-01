# Divide Into Chunks

## Description
Partition a sequence into consecutive groups of a requested maximum size. The final group may be shorter.

## Requirements
- Implement `chunks(items, size)` in `solution.py`.
- Return a new list of consecutive sublists containing at most `size` elements; assume `size` is positive.
- Preserve the original order and do not modify `items`.
- Return the result instead of printing it.
- Do not run input-handling code when the module is imported.

## Example
`chunks([1, 2, 3, 4, 5], 2)` → `[[1, 2], [3, 4], [5]]`.

## Tips
Consider the boundaries when the input length is not divisible by the group size.

The examples specify behavior without supplying the implementation.
