# Remember the Recent

## Description
Create a capacity-limited cache that discards its least recently used entry when another entry must be stored.

## Requirements
- Implement `LRUCache(capacity)` in `starter/solution.py`.
- Require positive capacity.
- Provide `get(key)` returning the value or `None` for a missing key.
- Provide `put(key, value)` to add or update an entry.
- Make successful reads and updates count as recent use.
- Evict the least recently used entry when insertion exceeds capacity.
- Use the Python standard library only. Do not print or request input at import time.

## Tips
- Why should a read change the order of future eviction?
- What happens when an existing key is updated?
- Think through valid and invalid operations and their effects on object state.

## Example Behavior
With capacity `2`, storing `a` and `b`, reading `a`, then storing `c` evicts `b`.
