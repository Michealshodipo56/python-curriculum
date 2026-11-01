# Select File Types

## Description
Filter filenames by their final extension while preserving the original order.

### Behavior contract
Given a list of filenames and a suffix, return filenames whose final suffix matches case-insensitively, preserving order. The suffix must include the dot.

## Requirements
- Implement `filter_suffix(names, suffix)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Match the final suffix, not a similar substring elsewhere in the name.

The task defines behavior; design the implementation independently.
