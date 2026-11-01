# Recognize File Extensions

## Description
Identify the final extension of a filename, including hidden-file edge cases.

### Behavior contract
Return the lowercase final extension including its dot from a filename. A leading dot on a dotfile does not count as an extension. Return empty string if none.

## Requirements
- Implement `file_extension(filename)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
A dot at the beginning of a hidden filename does not necessarily indicate an extension.

The task defines behavior; design the implementation independently.
