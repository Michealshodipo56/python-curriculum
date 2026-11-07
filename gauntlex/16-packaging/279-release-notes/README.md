# Write a Release Note

## Description
Turn a version identifier and change descriptions into a short, predictable Markdown announcement.

## Requirements
- Implement `release_notes(version, changes)` in `starter/solution.py`.
- Begin with the exact heading `# Release VERSION`.
- When changes exist, follow the heading with a blank line and one `- CHANGE` line per entry.
- End the result with a newline.
- When no changes exist, return only the heading and one newline.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why is the empty-change case formatted differently from a release with entries?

## Example Behavior
`release_notes('1.0.0', ['Initial release'])` → `'# Release 1.0.0\n\n- Initial release\n'`.
