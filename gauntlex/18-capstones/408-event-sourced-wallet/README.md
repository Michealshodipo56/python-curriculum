# Event-Sourced Wallet

## Description

Build a wallet whose balances are derived from an append-only history of credit and debit events.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements

- Run commands from `starter/` as `python main.py credit ACCOUNT AMOUNT`, `python main.py debit ACCOUNT AMOUNT`, `python main.py balance ACCOUNT`, or `python main.py history ACCOUNT`.
- Persist append-only events in SQLite at the path supplied by `WALLET_DB` across separate process runs.
- Amounts are positive integer cents. Invalid amounts exit with status `2` without recording an event.
- Successful `credit` and `debit` commands print `ok`. Record credits as positive deltas and debits as negative deltas.
- A debit exceeding the account balance prints `insufficient` and records no event.
- `balance` prints the account's integer balance, or `0` for an account with no events.
- `history` prints compact, sorted-key JSON objects in an array ordered by event ID, restricted to the requested account. Each object contains `id`, `account`, and integer `delta`.
- Keep accounts isolated, preserve history, and ensure replaying the account's events reproduces its balance. End each printed result with a newline.

## Constraints

- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables

- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how replay reconstructs balances and why rejected debits create no event.

## Design Considerations

Use append-only events as the source of truth. A rejected debit must leave the event history untouched, and replay must reproduce balances.

## Example Behavior

Credit 500 cents and debit 200 cents for one account: the balance is 300 cents, with two ordered history entries.

## Tips

A rejected debit must not leave an event behind. Every balance must be reproducible from history.

## Guide and Auditor

The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
