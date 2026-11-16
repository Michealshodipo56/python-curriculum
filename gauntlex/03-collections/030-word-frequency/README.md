# Word Tally

## Description

Write a program that reads a line of words and counts how many times each word appears. Print each word and its count as `WORD: COUNT`, in the order that word first appeared.

## Requirements

- Read one line of space-separated words; the line may be empty.
- Count occurrences of each distinct word using case-sensitive matching.
- Display one line per distinct word in the format `WORD: COUNT`.
- Order the lines by each word's first appearance.
- If the input is empty, produce no output.
- Do not print prompts or additional text.

## Tips

- Consider how a word can be associated with a running count.
- How can you avoid printing a word more than once?
- Think about the distinction between counting occurrences and ordering the report.

## Example Input

```text
cat dog cat
```

## Example Output

```text
cat: 2
dog: 1
```
