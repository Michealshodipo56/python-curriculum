# Publish and Listen

## Description
Connect named events to callback functions and dispatch notifications in a predictable order.

### Behavior contract
Implement EventEmitter with on(event,callback), off(event,callback), and emit(event,*args). Callbacks run in registration order. off removes one matching registration, if present; emit returns a list of callback return values.

## Requirements
- Define `EventEmitter` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
What happens when a callback is registered twice or removed once?

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
