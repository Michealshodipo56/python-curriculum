# chunklist

## Description
Implement `chunks(items, size)` returning consecutive sublists of at most `size` elements. Assume size is positive.

## Requirements
- Implement the named function in `solution.py`.
- Return the value; do not print it.
- Do not add executable input handling at module import time.

## Examples
`chunklist([1, 2, 3, 4, 5], 2)` → `[[1, 2], [3, 4], [5]]`

`chunklist([], 3)` → `[]`

## Tips
A slice can select a bounded section. Move the start position by the chunk size.
