# password_strength

## Challenge
Return a score 0–4, adding one point each for length>=12, at least one ASCII lowercase, at least one ASCII uppercase, and at least one ASCII digit. No entropy claims.

## Requirements
- Implement `password_strength(password)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
This is a simple rule score, not a security guarantee.

## Run tests
`python -m pytest tests -q`
