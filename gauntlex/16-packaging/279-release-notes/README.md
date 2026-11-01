# Write a Release Note

## Description
Generate a short Markdown release announcement from a version and list of changes.

### Behavior contract
Given version and a list of change descriptions, return Markdown with first line `# Release VERSION`, a blank line, then one `- CHANGE` line per change. End with a newline. For no changes, return only heading and newline.

## Requirements
- Implement `release_notes(version, changes)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
An empty change list should still produce a valid release heading.

The learner must develop the implementation from the stated contract.
