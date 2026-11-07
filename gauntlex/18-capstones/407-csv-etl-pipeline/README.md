# CSV Data Pipeline

## Description

Transform CSV records into validated, deduplicated JSON Lines using safe file replacement.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements

- Run `python main.py INPUT.csv OUTPUT.jsonl` from `starter/`; missing arguments exit with status `2`.
- Read a CSV file with header fields `id`, `name`, and `amount_cents`, and trim surrounding field whitespace.
- Require nonempty `id` and `name` and an integer `amount_cents` of at least zero. Skip invalid rows.
- Deduplicate by `id`, retaining the first valid row for each ID in original order. An invalid row must not reserve its ID.
- Write UTF-8 JSON Lines: one compact, sorted-key object per line with string `id`, string `name`, and integer `amount_cents`.
- Prepare the complete output in a temporary file and atomically replace the destination when writing succeeds.
- Print one compact, sorted-key JSON object with integer `written` and `skipped` counts, followed by a newline. Count both invalid rows and later duplicate IDs as skipped; do not count the header.

## Constraints

- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables

- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain validation order, duplicate handling, and atomic output replacement.

## Design Considerations

Validate each row before reserving its ID for deduplication. Write output to a temporary file and replace the destination only after the output is complete.

## Example Behavior

If an invalid row uses ID `x` before a valid row with ID `x`, the valid row may still be written as the first valid occurrence.

## Tips

Deduplication keeps the first valid row for each identifier; an invalid earlier row must not claim that identifier.

## Guide and Auditor

The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
