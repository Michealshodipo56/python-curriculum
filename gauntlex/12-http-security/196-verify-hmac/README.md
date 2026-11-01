# Verify a Signature

## Description
Check whether a supplied signature matches a message and secret, rejecting malformed signatures.

### Behavior contract
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
A secure comparison should not reveal where two signatures first differ.

Examples describe the contract, not a solution.
