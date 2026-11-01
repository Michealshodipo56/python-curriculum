# Remember the Recent

## Description
Build a fixed-capacity cache that discards the least recently used entry when it fills up.

### Behavior contract
Implement LRUCache(capacity) with get(key) and put(key,value). get returns None when missing. Accessing or updating an entry makes it most recently used; inserting beyond capacity evicts the least recently used. Capacity must be positive.

## Requirements
- Define `LRUCache` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
A read changes recency even if it does not change the stored value.

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
