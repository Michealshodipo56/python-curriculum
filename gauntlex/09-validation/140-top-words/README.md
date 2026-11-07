# Word Leaderboard

## Description

Extract words from text, count how often each appears, and rank them. Equal-frequency words must be ordered alphabetically.

## Requirements

- Implement `top_words(text, n)` in `starter/solution.py`.
- Assume `n` is a nonnegative integer.
- Recognize words as maximal runs of ASCII letters `a`–`z`, ignoring case.
- Count normalized lowercase words, treating punctuation and other characters as separators.
- Return at most `n` distinct words, ordered by descending frequency and then alphabetically.
- Return `[]` when `n` is zero or no words exist.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why must case normalization happen before counting?
- How should equal-frequency words be ordered?
- What separates two ASCII words?

## Example Behavior

`top_words('Red red blue!', 2)` → `['red', 'blue']`; `top_words('b a b a', 1)` → `['a']`.
