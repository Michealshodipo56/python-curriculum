# Read URL Parameters

## Description

A URL query string can contain encoded characters, blank values, and repeated names. Parse it into a mapping where later occurrences replace earlier values.

## Requirements

- Implement `parse_query(text)` in `starter/solution.py`.
- Return a dictionary of decoded parameter names and values.
- Decode percent escapes and interpret `+` as a space.
- Keep blank values.
- For repeated keys, retain the last decoded value.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why does `%2B` differ from a literal plus sign?
- What should happen when a name occurs more than once?

## Example Behavior

`parse_query('a=1&b=two+words&a=3')` → `{'a': '3', 'b': 'two words'}`; `parse_query('x=&y=%2B')` → `{'x': '', 'y': '+'}`.
