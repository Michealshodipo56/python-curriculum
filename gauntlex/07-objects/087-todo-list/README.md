# Track the Work

## Description
Create a task collection that distinguishes pending work from completed work.

### Behavior contract
Implement TodoList with add(title), complete(index), pending(), and completed(). Titles must be nonempty strings after trimming; indexes are zero-based insertion positions; invalid indexes raise IndexError. Return lists of titles.

## Requirements
- Define `TodoList` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
A task's insertion position and its completion state serve different purposes.

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
