# Opaque Page Cursor

## Description
Pagination APIs can encode a numeric offset into a URL-safe cursor. The token is a representation, not a security boundary.

## Requirements
- Implement `encode_cursor(offset)` in `starter/solution.py`.
- Accept a nonnegative integer offset.
- Raise `ValueError` for a negative offset.
- Encode the offset's ASCII decimal text using URL-safe Base64.
- Remove Base64 padding characters from the returned token.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why is URL-safe encoding useful for pagination links?
- Why should the cursor not be treated as encrypted?

## Example Behavior
`encode_cursor(0)` → `'MA'`; `encode_cursor(12)` → `'MTI'`.
