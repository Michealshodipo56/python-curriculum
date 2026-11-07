# Streaming Log Inspector

## Description
Create a tool that turns raw application logs into a reliable summary, ignoring invalid records.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Read UTF-8 lines from stdin in `LEVEL|YYYY-MM-DD|MESSAGE` format. LEVEL is INFO, WARN, or ERROR. Validate calendar dates, skip malformed lines, and count each level. Print one compact sorted-key JSON object with keys `total`, `INFO`, `WARN`, `ERROR`, and `dates`, where dates maps YYYY-MM-DD to the number of valid records on that date. Exit successfully even when input is empty. MESSAGE may contain additional pipe symbols.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Parse only the first two separators as structural delimiters; later pipes belong to the message. Validate dates as real calendar dates, not merely strings matching a pattern.

## Example Behavior
A valid `INFO|2026-01-01|start|ready` line counts as one INFO event; an impossible date does not contribute.

## Tips
The log message may contain extra separators. Only validated records should affect counts.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
