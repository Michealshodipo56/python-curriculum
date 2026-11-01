# One Line Ending

## Description
Convert different newline conventions into a consistent representation without losing content.

### Behavior contract
Convert CRLF and standalone CR line endings to LF. Preserve all other characters, including trailing newlines.

## Requirements
- Implement `normalize_line_endings(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Replacement order matters when two-character CRLF sequences are present.

The task defines behavior; design the implementation independently.
