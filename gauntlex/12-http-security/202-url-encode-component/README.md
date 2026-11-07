# Escape One URL Component

## Description

A path component is a single part of a URL, so characters such as spaces and slashes must be encoded rather than interpreted as separators.

## Requirements

- Implement `encode_component(text)` in `starter/solution.py`.
- Encode the input as UTF-8 and percent-escape reserved or unsafe bytes.
- Leave only RFC 3986 unreserved characters (`A`–`Z`, `a`–`z`, digits, `-`, `.`, `_`, `~`) unescaped.
- Encode spaces as `%20`, not `+`.
- Encode `/` as `%2F` because it belongs to the component's data.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips

- Why does a slash inside one component need escaping?
- How does URL component encoding differ from form encoding?

## Example Behavior

`encode_component("hello world")` → `"hello%20world"`

`encode_component("a/b")` → `"a%2Fb"`
