# Local Link Inspector

## Description
Inspect Markdown files for broken local links without contacting external websites.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Run python main.py ROOT. Recursively inspect Markdown files. Extract inline links [label](target) where target has no spaces or parentheses. Ignore http:, https:, mailto:, and # links. Remove query/fragment from local targets. Resolve relative to containing file; targets beginning / resolve under ROOT. Flag missing files and paths escaping ROOT, including symlinks. Print compact sorted-key JSON array {file,target} sorted by file and target. Exit 1 for broken links, else 0. Never make network requests.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Tips
A path can appear inside the project yet resolve outside it through traversal or a symbolic link.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
