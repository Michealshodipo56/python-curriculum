# Rule-Based Password Score

## Description
Score a password against four explicit character and length criteria.

### Behavior contract
Return a score 0–4, adding one point each for length>=12, at least one ASCII lowercase, at least one ASCII uppercase, and at least one ASCII digit. No entropy claims.

## Requirements
- Implement `password_strength(password)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
This simple score is not an estimate of actual password entropy or a security guarantee.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
