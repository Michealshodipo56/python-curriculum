# Encode Base64

## Description

Represent UTF-8 text as standard Base64, including required padding.

## Requirements

- Implement `base64_encode(text)` in `starter/solution.py`.
- Return standard Base64 encoding of the UTF-8 bytes of text, including padding.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Encode UTF-8 bytes using standard Base64, retaining any required `=` padding. Base64 is a reversible representation, not encryption.

## Tips

Base64 encodes bytes and does not provide confidentiality.

## Example Behavior

`base64_encode('Hi')` → `'SGk='`.
