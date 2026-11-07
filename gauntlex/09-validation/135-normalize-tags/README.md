# Clean the Tags

## Description

Normalize comma-separated labels into a unique, ordered collection of meaningful tags.

## Requirements

- Implement `normalize_tags(text)` in `starter/solution.py`.
- Split input text at commas.
- Trim surrounding whitespace and lowercase each tag.
- Discard empty tags after trimming.
- Remove duplicates while retaining the first occurrence of each normalized tag.
- Return a list of tags, or `[]` if none remain.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why must normalization happen before duplicate detection?
- What should consecutive commas contribute?

## Example Behavior

`normalize_tags('Python, python, AI, , ai')` → `['python', 'ai']`; `normalize_tags(' , ')` → `[]`.
