# Protect a Private Route

## Description
Require a valid bearer token before returning a protected resource.

### Behavior contract
Implement GET `/private` requiring Authorization header `Bearer secret-token` (scheme case-insensitive). Valid authorization returns 200 and body `welcome`; otherwise 401 and body `unauthorized`. Use a timing-resistant token comparison.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
Compare secrets without revealing where two token strings differ.

Build the response behavior yourself without a provided implementation.
