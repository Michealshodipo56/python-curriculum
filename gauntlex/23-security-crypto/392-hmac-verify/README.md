# hmac_verify

## Challenge
Return True only if lowercase or uppercase hexadecimal signature equals the HMAC-SHA256 signature of UTF-8 message with UTF-8 secret. Reject malformed signatures by returning False. Use constant-time comparison.

## Requirements
- Implement `hmac_verify(secret, message, signature)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Use hmac.compare_digest for the final comparison.

## Run tests
`python -m pytest tests -q`
