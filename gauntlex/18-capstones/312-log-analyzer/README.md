# Log Analyzer CLI

## Project brief
Build a streaming log analyzer that summarizes valid application logs.

## Acceptance contract
Read UTF-8 lines from stdin in `LEVEL|YYYY-MM-DD|MESSAGE` format. LEVEL is INFO, WARN, or ERROR. Validate calendar dates, skip malformed lines, and count each level. Print one compact sorted-key JSON object with keys `total`, `INFO`, `WARN`, `ERROR`, and `dates`, where dates maps YYYY-MM-DD to the number of valid records on that date. Exit successfully even when input is empty. MESSAGE may contain additional pipe symbols.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the complete working project in `starter/main.py` and any additional modules under `starter/`.
- Add your own unit and integration tests beyond the provided acceptance checks.
- Document architecture, failure modes, and how to run the program.

## AI Guide policy
The Guide may ask about architecture, input contracts, and debugging, but must never provide full code or a working answer.

## AI Auditor defense
Explain your architecture, show a passing end-to-end test, and justify how you handle invalid inputs and persistence or service lifecycle.
