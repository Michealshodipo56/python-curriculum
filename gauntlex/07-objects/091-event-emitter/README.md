# Publish and Listen

## Description

Build an event emitter that associates named events with callback functions and dispatches notifications in registration order.

## Requirements

- Implement `EventEmitter` in `starter/solution.py`.
- Provide `on(event, callback)` to register a callback.
- Provide `off(event, callback)` to remove one matching registration, if present.
- Provide `emit(event, *args)` to call listeners in registration order and return their results as a list.
- Use the Python standard library only. Do not print or request input at import time.

## Tips

- What happens if a callback is registered twice but removed only once?
- Why does listener order matter?

## Example Behavior

If two callbacks return `1` and `2`, emitting their event returns `[1, 2]`.
