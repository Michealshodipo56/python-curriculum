# Read an INI Section

## Description
Configuration files group assignments under named sections. Read only one section while respecting whitespace and comments.

## Requirements
- Implement `parse_ini_section(text, section)` in `starter/solution.py`.
- Recognize section headers `[name]` and assignments `key=value` in well-formed text.
- Trim surrounding whitespace from keys and values.
- Ignore blank lines and lines beginning `#` or `;`.
- Return entries from the requested section, with later duplicate keys overriding earlier ones.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Track the active section as lines are read, and apply assignments only while the requested section is active. Later duplicate keys in that section replace earlier values.

## Tips
- How can the current section be tracked while reading line by line?

## Example Behavior
`parse_ini_section('[db]\nhost=local\n[app]\nmode=dev', 'db')` → `{'host': 'local'}`.
