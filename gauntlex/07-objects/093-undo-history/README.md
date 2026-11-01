# Step Back in Time

## Description
Keep enough history to restore earlier values one change at a time.

### Behavior contract
Implement UndoHistory(initial) with set(value), undo(), and current property. undo restores the previous value; undo with no previous value raises IndexError.

## Requirements
- Define `UndoHistory` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
Which value must be saved before applying a new one?

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
