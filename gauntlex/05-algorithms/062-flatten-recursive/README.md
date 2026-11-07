# Unfold Nested Lists

## Description

A nested list may contain integers and more lists at arbitrary depths. Traverse the structure and return all integers in their original left-to-right order.

## Requirements

- Implement `flatten_recursive(items)` in `starter/solution.py`.
- Assume elements are integers or lists following the same rule at any depth.
- Return a new flat list containing every integer in encounter order.
- Handle empty lists at any depth.
- Do not modify input, print, or execute code on import.

## Tips

- What is the difference between encountering an integer and encountering another list?
- How does the same decision recur inside nested lists?

## Example Behavior

`flatten_recursive([1, [2, [3]], 4])` → `[1, 2, 3, 4]`; `flatten_recursive([])` → `[]`.
