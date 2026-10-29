# read_config

## Challenge
Given a mapping of environment variables, return {'debug':bool,'port':int}. DEBUG is true for 1/true/yes (case-insensitive), otherwise false. PORT defaults to 8000 and must be an integer 1–65535; invalid PORT raises ValueError.

## Requirements
- Implement `read_config(env)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Parse configuration at startup and reject invalid ports.

## Run tests
`python -m pytest tests -q`
