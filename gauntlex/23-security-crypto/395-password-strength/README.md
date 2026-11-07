# Rule-Based Password Score

## Description

Score a password against four explicit character and length criteria.

## Requirements

- Implement `password_strength(password)` in `starter/solution.py`.
- Return a score 0–4, adding one point each for length>=12, at least one ASCII lowercase, at least one ASCII uppercase, and at least one ASCII digit. No entropy claims.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Score only the four stated rules: minimum length, ASCII lowercase, ASCII uppercase, and ASCII digit. This educational score does not measure password entropy or guarantee security.

## Tips

This simple score is not an estimate of actual password entropy or a security guarantee.

## Example Behavior

`password_strength('Abcdefghij12')` → `4`; `password_strength('abc')` → `1`.
