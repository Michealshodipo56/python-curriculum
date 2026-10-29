# HTTP JSON API Server

## Project brief
Build a minimal HTTP JSON service using only Python's standard library.

## Acceptance contract
`main.py` must start an HTTP server on 127.0.0.1 and the port given by `PORT` (positive integer). Implement GET `/health` returning status 200 and JSON `{"status":"ok"}`; GET `/echo?message=TEXT` returning status 200 and JSON `{"message":"TEXT"}` with percent and plus decoding; all other paths return status 404 and JSON `{"error":"not found"}`. Send Content-Type `application/json`. Serialize responses as compact JSON. Shut down cleanly when terminated. Avoid printing request logs to stdout.

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
