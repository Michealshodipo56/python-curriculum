# Fingerprint a Message

## Description
A cryptographic digest turns a message into a fixed-length fingerprint. In this challenge, generate the SHA-256 fingerprint of text encoded as UTF-8 and present the digest in a consistent hexadecimal form.

## Requirements
- Implement `sha256_hex(text)` in `starter/solution.py`.
- Encode the input string as UTF-8 before hashing.
- Return the SHA-256 digest as exactly 64 lowercase hexadecimal characters.
- Return the result without printing, prompting, or making network requests.
- Use Python's standard library only.

## Tips
- Hash functions operate on bytes, not directly on Python characters.
- The hexadecimal digest represents the hash output, not the original message.
- Even an empty string has a well-defined digest.

## Example Behavior
`sha256_hex("")` → `"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"`

`sha256_hex("abc")` → `"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"`
