# CSV Data Pipeline

## Description
Transform CSV records into validated, deduplicated JSON Lines using safe file replacement.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Run python main.py INPUT.csv OUTPUT.jsonl. CSV header id,name,amount_cents. Trim fields; require nonempty id/name and nonnegative integer amount. Skip invalid rows; deduplicate by id keeping first valid row. Write compact sorted-key JSONL in original order using temporary file and atomic replacement. Print compact sorted-key JSON {written:N,skipped:M}. Missing args exit 2.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Validate each row before reserving its ID for deduplication. Write output to a temporary file and replace the destination only after the output is complete.

## Example Behavior
If an invalid row uses ID `x` before a valid row with ID `x`, the valid row may still be written as the first valid occurrence.

## Tips
Deduplication keeps the first valid row for each identifier; an invalid earlier row must not claim that identifier.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
