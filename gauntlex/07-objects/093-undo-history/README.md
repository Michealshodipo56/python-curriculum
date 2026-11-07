# Step Back in Time

## Description

Maintain a current value together with enough history to restore earlier values, one change at a time.

## Requirements

- Implement `UndoHistory(initial)` in `starter/solution.py`.
- Provide `set(value)` to replace the current value and preserve the previous one.
- Expose the active value through the `current` property.
- Provide `undo()` to restore and return the preceding value.
- Raise `IndexError` when there is no earlier state.
- Use the Python standard library only. Do not print or request input at import time.

## Tips

- What should be saved before each change?
- How does the history change after an undo?

## Example Behavior

Starting at `'A'`, setting `'B'` then `'C'` and undoing once restores `'B'`.
