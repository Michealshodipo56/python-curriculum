# Opaque Page Cursor

## Description
Encode a nonnegative offset as a URL-safe, unpadded cursor token.

### Behavior contract
Given a nonnegative integer offset, return a URL-safe Base64 string without padding encoding its ASCII decimal representation. Raise ValueError for negative offsets.

## Requirements
- Implement `encode_cursor(offset)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
A cursor is a representation of an offset, not an encryption of it.

Design your own implementation from the specified behavior.
