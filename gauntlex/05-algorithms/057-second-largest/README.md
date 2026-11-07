# Runner-Up Value

## Description
The second-largest distinct value is not always the second item in descending order. Find the runner-up value while ignoring repeated copies of the maximum.

## Requirements
- Implement `second_largest(items)` in `solution.py`.
- Return the second-largest distinct integer.
- Return `None` when fewer than two distinct values exist.
- Support negative integers and duplicate values.
- Do not modify input, print, or execute code on import.

## Tips
- Why should two copies of the maximum not occupy both ranks?
- Consider an all-equal list and a list of negative numbers.

## Example Behavior
`second_largest([3, 1, 3, 2])` → `2`; `second_largest([5, 5])` → `None`.
