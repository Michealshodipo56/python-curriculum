# Last In, First Out

## Description
A stack stores values so the newest addition is the first one removed. Model this behavior as an object whose state changes across method calls.

## Requirements
- Define `Stack` in `starter/solution.py`.
- Provide `push(value)` to add an item and `pop()` to remove and return the newest item.
- Provide `peek()` to return the newest item without removing it.
- Provide `is_empty()` to report whether any items remain.
- Raise `IndexError` for `pop()` or `peek()` on an empty stack.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- How does the most recent addition affect the next removal?
- What should change after a peek compared with a pop?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
After pushing `4` and then `9`, `peek()` returns `9`; `pop()` returns `9`, then `4`.
