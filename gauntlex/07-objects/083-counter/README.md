# Count by Key

## Description
Create an object that remembers how many times each key has been recorded.

### Behavior contract
Implement CounterMap with add(key), count(key), and total(). Adding increments the key's count by one; absent keys have count zero; total returns the number of adds.

## Requirements
- Define `CounterMap` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
A missing key has never been seen; how should it be represented?

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
