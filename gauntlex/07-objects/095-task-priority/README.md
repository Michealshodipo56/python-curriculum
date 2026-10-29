# prioritytasks

## Description
Implement PriorityTasks with add(title,priority) and pop(). Lower integer priority values come first. Equal priorities retain insertion order. pop returns the title; popping empty raises IndexError.

## Requirements
- Define `PriorityTasks` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Examples
The tests exercise the class methods and expected state changes.

## Tips
A heap with a monotonically increasing insertion counter can break ties.
