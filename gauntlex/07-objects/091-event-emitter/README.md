# eventemitter

## Description
Implement EventEmitter with on(event,callback), off(event,callback), and emit(event,*args). Callbacks run in registration order. off removes one matching registration, if present; emit returns a list of callback return values.

## Requirements
- Define `EventEmitter` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Examples
The tests exercise the class methods and expected state changes.

## Tips
Map event names to ordered callback lists; don't assume every event has listeners.
