# URL-Friendly Words

## Description
Page titles are often turned into compact URL identifiers. Normalize casing and separate words consistently, even when punctuation and whitespace appear together.

## Requirements
- Implement `slugify(text)` in `starter/solution.py`.
- Return a lowercase, hyphen-separated identifier based on the supplied title.
- Treat punctuation, whitespace, and underscores as boundaries between retained word content.
- Avoid leading, trailing, or repeated hyphens; return an empty slug if nothing remains.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- What happens when several separators occur consecutively?
- How should leading or trailing punctuation affect the output?

## Example Behavior
`slugify("Hello, Python World!")` → `"hello-python-world"`

`slugify("  A__B  ")` → `"a-b"`
