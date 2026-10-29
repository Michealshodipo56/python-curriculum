# request_id

## Challenge
Return a lowercase hexadecimal UUID version 4 string with hyphens, using a secure standard-library UUID generator. Each call should normally return a new identifier.

## Requirements
- Implement `request_id()` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
See the contract and write additional edge-case tests.

## Tips
The uuid module generates random version-4 identifiers.
