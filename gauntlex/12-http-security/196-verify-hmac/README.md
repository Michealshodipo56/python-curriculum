# verify_hmac

## Challenge
Return True when the supplied lowercase hex signature matches HMAC-SHA256(secret,message). Treat malformed signatures as False.

## Requirements
- Implement `verify_hmac(secret, message, signature)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`verify_hmac("key", "abc", "wrong")` → `False`

`verify_hmac("key", "abc", "")` → `False`

## Tips
Compute the expected signature and compare it using a timing-resistant primitive.
