# Verify a Signature

## Description

A received message may be accompanied by a claimed HMAC. Determine whether the signature matches the shared secret and message, using a timing-resistant comparison.

## Requirements

- Implement `verify_hmac(secret, message, signature)` in `starter/solution.py`.
- Recompute HMAC-SHA256 for the supplied UTF-8 secret and message.
- Return `True` only if the supplied lowercase hexadecimal signature matches the expected digest.
- Return `False` for malformed or mismatched signatures.
- Use a timing-resistant comparison rather than an ordinary early-exit string check.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips

- Why should malformed signatures be treated as invalid?
- Why can comparison timing matter for authentication?

## Example Behavior

`verify_hmac("key", "abc", "wrong")` → `False`

`verify_hmac("key", "abc", "")` → `False`
