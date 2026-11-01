# Event-Sourced Wallet

## Description
Build a wallet whose balances are derived from an append-only history of credit and debit events.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Use SQLite WALLET_DB path. Commands credit ACCOUNT AMOUNT, debit ACCOUNT AMOUNT, balance ACCOUNT, history ACCOUNT. Amounts are positive integer cents. credit/debit print ok; insufficient debit prints insufficient without recording an event. balance prints integer. history prints compact sorted-key JSON array of {id,account,delta} in event ID order. Events are append-only; balances must be reproducible by replay. Invalid amounts exit 2.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Tips
A rejected debit must not leave an event behind. Every balance must be reproducible from history.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
