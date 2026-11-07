# Fingerprint Configuration

## Description
Configuration fingerprints should remain identical when dictionaries contain the same data in different insertion orders. Canonicalize structured content before hashing.

## Requirements
- Implement `config_fingerprint(config)` in `starter/solution.py`.
- Accept a JSON-compatible configuration value.
- Serialize it as compact JSON with dictionary keys sorted.
- Encode the canonical representation as UTF-8 and hash with SHA-256.
- Return the lowercase hexadecimal digest; do not mutate the configuration.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- Why does sorting dictionary keys matter for reproducible hashes?

## Example Behavior
`config_fingerprint({'a': 1, 'b': 2})` and `config_fingerprint({'b': 2, 'a': 1})` return the same digest.
