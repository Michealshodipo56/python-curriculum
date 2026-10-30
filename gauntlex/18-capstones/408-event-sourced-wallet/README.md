# Event-Sourced Wallet

## Project brief and acceptance criteria
Use SQLite WALLET_DB path. Commands credit ACCOUNT AMOUNT, debit ACCOUNT AMOUNT, balance ACCOUNT, history ACCOUNT. Amounts are positive integer cents. credit/debit print ok; insufficient debit prints insufficient without recording an event. balance prints integer. history prints compact sorted-key JSON array of {id,account,delta} in event ID order. Events are append-only; balances must be reproducible by replay. Invalid amounts exit 2.

## Deliverables
Implement in starter/main.py, add unit tests and document architecture. Python 3.11+ standard library only. No network services. Do not print debug output to stdout. Use parameterized SQL where applicable.

## Run
python -m pytest tests -q
