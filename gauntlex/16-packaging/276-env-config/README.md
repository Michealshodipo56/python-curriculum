# Read Environment Settings

## Description
Application configuration often arrives as text from environment variables. Interpret the supported values while applying a safe default only when a setting is absent.

## Requirements
- Implement `read_config(env)` in `starter/solution.py`.
- Accept a mapping of environment variable names to strings.
- Return a dictionary with boolean `debug` and integer `port`.
- Set `debug` to `True` for `DEBUG` values `1`, `true`, or `yes`, ignoring case; otherwise `False`.
- Use port `8000` when `PORT` is absent.
- Raise `ValueError` unless a supplied port is an integer from 1 through 65535.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why should an invalid supplied port not silently fall back to the default?

## Example Behavior
`read_config({'DEBUG': 'YES', 'PORT': '9000'})` → `{'debug': True, 'port': 9000}`.
