# First In, First Out

## Description
A queue represents a waiting line: items leave in the same order in which they arrive. Build an object that maintains that order through repeated operations.

## Requirements
- Define `Queue` in `starter/solution.py`.
- Provide `enqueue(value)` to add an item at the back.
- Provide `dequeue()` to remove and return the oldest waiting item.
- Provide `is_empty()` to report whether the queue contains items.
- Raise `IndexError` when `dequeue()` is called on an empty queue.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- How does this removal order differ from a stack?
- Consider what happens when several items are added before any are removed.
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
After enqueuing `'A'` and `'B'`, successive calls to `dequeue()` return `'A'` and `'B'`.
