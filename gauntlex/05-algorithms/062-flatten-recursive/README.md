# Unfold Nested Lists

## Description
Traverse a structure containing integers and lists nested to any depth, producing a single left-to-right sequence.

## Requirements
- Implement `flatten_recursive(items)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`flatten_recursive([1, [2, [3]], 4])` → `[1, 2, 3, 4]`

`flatten_recursive([])` → `[]`

## Tips
What should happen when an element is an integer versus another list? The same question recurs at each nesting level.

The examples illustrate expected behavior, not an implementation.
