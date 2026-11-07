# Streaming Log Inspector

## Description

Create a tool that turns raw application logs into a reliable summary, ignoring invalid records.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements

- Run `python main.py` from `starter/` and read UTF-8 log lines from standard input.
- Each record has the form `LEVEL|YYYY-MM-DD|MESSAGE`. Only `INFO`, `WARN`, and `ERROR` are supported levels.
- Validate real calendar dates. Skip malformed records and impossible dates without counting them.
- The first two pipes separate fields; additional pipes remain part of the message.
- Print one compact JSON object with sorted keys: `total`, `INFO`, `WARN`, `ERROR`, and `dates`.
- `total` is the number of valid records; each severity key contains its count, including zero. `dates` maps each encountered valid date to its record count.
- Empty input succeeds with zero counts and an empty `dates` object. End the JSON output with a newline.

## Constraints

- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables

- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain record validation and how invalid records affect totals.

## Design Considerations

Parse only the first two separators as structural delimiters; later pipes belong to the message. Validate dates as real calendar dates, not merely strings matching a pattern.

## Example Behavior

A valid `INFO|2026-01-01|start|ready` line counts as one INFO event; an impossible date does not contribute.

## Tips

The log message may contain extra separators. Only validated records should affect counts.

## Guide and Auditor

The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
