# One Line Ending

## Description
Text copied between operating systems may contain CRLF, CR, or LF line endings. Standardize line boundaries without modifying other content.

## Requirements
- Implement `normalize_line_endings(text)` in `starter/solution.py`.
- Replace every CRLF and standalone CR line ending with LF.
- Preserve all other characters, including existing LF and trailing newlines.
- Return the normalized text without writing to disk.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Treat CRLF as one boundary before processing lone CR characters; otherwise a single Windows newline could become two line breaks. Preserve the presence or absence of a trailing newline.

## Tips
- Why does handling two-character line endings require care?

## Example Behavior
`normalize_line_endings('a\r\nb\rc\n')` → `'a\nb\nc\n'`.
