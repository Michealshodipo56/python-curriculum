# Read an INI Section

## Description
Extract configuration entries from one named section of an INI-style document.

### Behavior contract
Parse a simple INI string and return key/value pairs from the requested section. Section headers are `[name]`; entries are `key=value`; trim surrounding whitespace; skip blank lines and lines starting # or ;. Last duplicate wins. Assume well-formed input.

## Requirements
- Implement `parse_ini_section(text, section)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Track the active section while processing each line.

The task defines behavior; design the implementation independently.
