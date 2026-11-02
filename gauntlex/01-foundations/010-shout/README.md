# Clean Announcement

## Description
Messages received from users may contain unwanted whitespace at their boundaries and inconsistent capitalization. Prepare a message for announcement by normalizing its appearance without changing the spaces between its words.

## Requirements
- Read one line of text from standard input.
- Remove leading and trailing whitespace.
- Convert all remaining letters to uppercase.
- Preserve any whitespace that remains between characters.
- Display the resulting message on one line without prompts.

## Tips
- Investigate how leading and trailing whitespace differs from spaces inside a sentence.
- Think about the order in which text transformations can be applied.
- Consider what should be displayed when the input contains only whitespace.

## Example Input
```text
  hello Gauntlex  
```

## Example Output
```text
HELLO GAUNTLEX
```
