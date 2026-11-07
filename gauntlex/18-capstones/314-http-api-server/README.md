# A Minimal HTTP Service

## Description

Build a small local HTTP API with a health endpoint, an echo endpoint, and predictable JSON errors.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements

- Run `python main.py` from `starter/` to start a local HTTP server bound to `127.0.0.1` at the positive integer port supplied in `PORT`.
- GET `/health` returns HTTP `200` and JSON `{"status":"ok"}`.
- GET `/echo?message=TEXT` returns HTTP `200` and JSON `{"message":"TEXT"}`, decoding percent escapes and plus-as-space query encoding.
- Other paths return HTTP `404` and JSON `{"error":"not found"}`.
- Send `Content-Type: application/json` and encode responses as compact JSON.
- Keep request logs and debugging output off standard output. Release server resources when the process terminates.

## Constraints

- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables

- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain request parsing, response encoding, and server lifecycle.

## Design Considerations

Separate URL path matching from query-string parsing, and encode all responses consistently as compact JSON. Keep request logs off stdout.

## Example Behavior

A GET request to `/health` returns HTTP 200 and `{"status":"ok"}`; an unknown path returns HTTP 404 with the specified JSON error.

## Tips

A request's path and query parameters are different parts of its URL. Keep response encoding consistent.

## Guide and Auditor

The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
