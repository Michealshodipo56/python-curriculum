# Unique Request Identifier

## Description

Distributed systems use request identifiers to connect logs and trace related work. Generate a fresh identifier in canonical UUID version-four form.

## Requirements

- Implement `request_id()` in `starter/solution.py`.
- Return a lowercase UUID version 4 string with hyphens in canonical positions.
- Use a secure standard-library UUID generator.
- Generate a fresh identifier on each call rather than returning a fixed value.
- Do not print or make network requests.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips

- Why should the identifier include both a recognizable version and a consistent format?
- Why is a hard-coded identifier unsuitable?

## Example Behavior

Two calls return different strings, each in the form `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`, where each `x` is a lowercase hexadecimal digit and `y` is `8`, `9`, `a`, or `b`. No particular random identifier is required.
