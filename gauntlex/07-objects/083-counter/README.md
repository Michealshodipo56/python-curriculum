# Count by Key

## Description
A counter can record how often different values are observed. Design an object that tracks counts by key and also remembers the total number of recorded observations.

## Requirements
- Define `CounterMap` in `starter/solution.py`.
- Implement `add(key)` to increase that key's count by one.
- Implement `count(key)` to return the recorded count, or `0` for an unseen key.
- Implement `total()` to return the number of `add` calls across all keys.
- Maintain the state between calls without requiring interactive input.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- How should an unseen key be treated?
- Why is the overall total different from the number of distinct keys?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
After `add('red')`, `add('blue')`, and `add('red')`, `count('red')` is `2` and `total()` is `3`.
