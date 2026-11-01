# Read Environment Settings

## Description
Interpret application settings from environment-like key-value data with safe defaults.

### Behavior contract
Given a mapping of environment variables, return {'debug':bool,'port':int}. DEBUG is true for 1/true/yes (case-insensitive), otherwise false. PORT defaults to 8000 and must be an integer 1–65535; invalid PORT raises ValueError.

## Requirements
- Implement `read_config(env)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Some settings are optional; invalid ports must not silently fall back to a default.

The learner must develop the implementation from the stated contract.
