# First In, First Out

## Description
Model a waiting line where items leave in the order they arrive.

### Behavior contract
Implement a Queue class with enqueue(value), dequeue(), and is_empty(). Dequeue from an empty queue must raise IndexError.

## Requirements
- Define `Queue` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
What operations become expensive if every removal shifts all remaining elements?

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
