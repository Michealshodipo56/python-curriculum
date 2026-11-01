# Serve by Priority

## Description
Schedule tasks by urgency while preserving insertion order among equally urgent tasks.

### Behavior contract
Implement PriorityTasks with add(title,priority) and pop(). Lower integer priority values come first. Equal priorities retain insertion order. pop returns the title; popping empty raises IndexError.

## Requirements
- Define `PriorityTasks` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
A numeric priority alone cannot distinguish which equal-priority task arrived first.

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
