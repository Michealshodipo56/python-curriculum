# Stable Request Identity

## Description
A cache key should consistently identify the same request inputs. Combine the method, URL, and body into an unambiguous canonical representation before hashing.

## Requirements
- Implement `cache_key(method, url, body)` in `starter/solution.py`.
- Uppercase the request method before serialization.
- Represent the normalized method, URL, and optional body as a three-element JSON list in that order.
- Serialize JSON using compact separators and UTF-8 encoding.
- Return the SHA-256 digest as lowercase hexadecimal text.
- Do not make network requests.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why can directly concatenating fields be ambiguous?
- Why should method capitalization not change the resulting key?

## Example Behavior
See the contract and write additional edge-case tests.
