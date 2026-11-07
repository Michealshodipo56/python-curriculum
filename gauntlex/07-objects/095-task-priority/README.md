# Serve by Priority

## Description
Schedule tasks by urgency while preserving arrival order when two tasks have the same priority.

## Requirements
- Implement `PriorityTasks` in `starter/solution.py`.
- Provide `add(title, priority)` with integer priority values.
- Provide `pop()` returning the title with the lowest numeric priority.
- For equal priorities, return tasks in their insertion order.
- Raise `IndexError` when popping an empty collection.
- Use the Python standard library only. Do not print or request input at import time.

## Tips
- Why is a numeric priority alone insufficient to distinguish ties?
- What information preserves fairness for equally urgent tasks?
- Think through valid and invalid operations and their effects on object state.

## Example Behavior
Adding `A` at priority `2`, `B` at priority `1`, and `C` at priority `1` yields pops `B`, `C`, `A`.
