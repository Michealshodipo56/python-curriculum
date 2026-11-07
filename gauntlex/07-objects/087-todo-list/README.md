# Track the Work

## Description

A to-do list needs to preserve the order tasks were added while tracking whether each one has been completed. Build a stateful task manager.

## Requirements

- Define `TodoList` in `starter/solution.py`.
- Implement `add(title)` to store a title with surrounding whitespace removed; raise `ValueError` if nothing remains.
- Implement `complete(index)` using zero-based insertion positions.
- Raise `IndexError` for invalid task positions.
- Implement `pending()` and `completed()` to return lists of task titles in insertion order.
- Use Python's standard library only and do not print or request input at import time.

## Tips

- Why is a task's original position different from its completion state?
- What should happen when an invalid index is supplied?

## Example Behavior

After adding `'Read'` and `'Write'`, completing index `0` leaves `'Write'` pending and `'Read'` completed.
