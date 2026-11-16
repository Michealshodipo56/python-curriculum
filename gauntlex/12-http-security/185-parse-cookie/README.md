# Read Cookie Pairs

## Description

Implement `parse_cookie(text)` in `starter/solution.py`. Ignore empty segments and trim spaces around names and values.

## Requirements

- Implement `parse_cookie(text)` in `starter/solution.py`.
- Ignore empty segments and trim spaces around names and values.
- Split each assignment at its first equals sign.
- Keep the last value for repeated cookie names.
- Do not percent-decode values.
- Use Python's standard library without printing or making network requests.

## Tips

- **Concept to understand:** Parse semicolon-separated cookie assignments without decoding their contents.
- Why might a cookie value contain an equals sign?

## Example Behavior

`parse_cookie("a=1; theme=dark")` → `{"a": "1", "theme": "dark"}`

`parse_cookie("a=1; a=2; ")` → `{"a": "2"}`
